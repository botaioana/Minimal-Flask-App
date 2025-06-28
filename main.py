from flask import Flask, request
import subprocess
import pickle
import os
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    return "Bun venit la aplicația extrem de nesigură!"

# ⚠️ 1. Command Injection (CWE-78)
@app.route('/cmd')
def execute_command():
    cmd = request.args.get('command', 'whoami')
    return subprocess.check_output(cmd, shell=True)  # NESIGUR: shell=True cu input direct

# ⚠️ 2. SQL Injection (CWE-89)
@app.route('/login')
def login():
    username = request.args.get('user')
    password = request.args.get('pass')
    query = f"SELECT * FROM users WHERE user='{username}' AND pass='{password}'"  # NESIGUR: concatenare directă
    return f"Executing: {query}"

# ⚠️ 3. Insecure Deserialization (CWE-502)
@app.route('/deserialize')
def deserialize():
    data = request.args.get('data')
    return pickle.loads(bytes.fromhex(data))  # NESIGUR: deserializare nesigură

# ⚠️ 4. XSS (CWE-79)
@app.route('/xss')
def xss():
    user_input = request.args.get('input', '<script>alert("XSS")</script>')
    return f"<div>{user_input}</div>"  # NESIGUR: fără escapare

# ⚠️ 5. Path Traversal (CWE-22)
@app.route('/read')
def read_file():
    filename = request.args.get('file', '../../etc/passwd')
    with open(filename, 'r') as f:  # NESIGUR: acces la fișiere fără validare
        return f.read()

# ⚠️ 6. Hardcoded Secret (CWE-798)
API_KEY = "SUPER_SECRET_123"  # NESIGUR: cheie hardcodată

# ⚠️ 7. Debug Mode Enabled (CWE-489)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # NESIGUR: debug în producție
