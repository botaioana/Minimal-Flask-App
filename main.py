from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "Salut! Aplicația funcționează corect!"

@app.route('/health')
def health():
    return "OK", 200

# Endpoint vulnerabil la command injection
@app.route('/ping')
def ping():
    host = request.args.get('host', '127.0.0.1')
    output = os.popen(f"ping -c 1 {host}").read()  # ⚠️ Command Injection
    return f"<pre>{output}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # ⚠️ debug=True în producție e vulnerabil
