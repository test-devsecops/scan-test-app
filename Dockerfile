# Dockerfile (vulnerable)
FROM python:3.7  # old and unsupported version

# Critical vuln: running as root user (default)
WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Expose port (best practice missing: no non-root user)
EXPOSE 5000

CMD ["python", "app.py"]
