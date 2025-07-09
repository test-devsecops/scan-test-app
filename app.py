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

@app.route('/ping')
def ping():
    ip = request.args.get('ip')
    return subprocess.getoutput(f"ping -c 1 {ip}") 
    # test

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
