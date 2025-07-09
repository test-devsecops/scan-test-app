from flask import Flask, request
import sqlite3
import subprocess

app = Flask(__name__)

@app.route('/user')
def get_user():
    username = request.args.get('username')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"  
    result = cursor.execute(query).fetchall()
    conn.close()
    return str(result)

# testing

@app.route('/ping')
def ping():
    ip = request.args.get('ip')
    return subprocess.getoutput(f"ping -c 1 {ip}") 
    # test
 
# test_2
username = "admin"
password = "supersecret"

import subprocess
ip = input("Enter IP: ")
subprocess.call("ping " + ip, shell=True)

import ssl
import urllib.request
context = ssl._create_unverified_context()
urllib.request.urlopen("https://example.com", context=context)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
