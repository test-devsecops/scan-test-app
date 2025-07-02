# main.tf (vulnerable Terraform IaC)
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "bad_bucket" {
  bucket = "my-public-bucket-${random_id.bucket_id.hex}"
  acl    = "public-read"  # Critical vuln: public S3 bucket

  tags = {
    Name        = "InsecureBucket"
    Environment = "Dev"
  }
}

resource "random_id" "bucket_id" {
  byte_length = 4
}

resource "aws_security_group" "open_sg" {
  name        = "open_sg"
  description = "Allow all inbound traffic"

  ingress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]  # Critical vuln: open to the world
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
