from flask import Flask, request
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Bun venit la aplicația extrem de nesigură!"

# ⚠️ 1. Command Injection (CWE-78) - DETECTAT (Critical)
@app.route('/cmd')
def execute_command():
    cmd = request.args.get('command', 'whoami')
    return subprocess.check_output(cmd, shell=True)  # Linia 17

# ⚠️ 4. XSS (CWE-79) - DETECTAT (Medium) x2
@app.route('/xss')
def xss():
    user_input = request.args.get('input', '<script>alert("XSS")</script>')
    return f"<div>{user_input}</div>"  # Linia 25/37 (două detectări)

# ⚠️ 5. Path Traversal (CWE-22) - DETECTAT (High)
@app.route('/read')
def read_file():
    filename = request.args.get('file', '../../etc/passwd')
    with open(filename, 'r') as f:  # Linia 43
        return f.read()

# ⚠️ 7. Debug Mode Enabled (CWE-489) - DETECTAT (High)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # Linia 51
