from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/')
def hello():
    return "Salut! Aplicația funcționează corect!"

@app.route('/health')
def health():
    return "OK", 200

# ⚠️ Command Injection — subprocess cu input nesanitizat
@app.route('/ping')
def ping():
    host = request.args.get('host', '127.0.0.1')
    output = subprocess.check_output(f"ping -c 1 {host}", shell=True)  # GHAS vede asta
    return f"<pre>{output.decode()}</pre>"

# ⚠️ Eval Injection — code execution
@app.route('/eval')
def eval_test():
    code = request.args.get('code', 'print("no code")')
    result = eval(code)  # GHAS va detecta asta garantat
    return f"<pre>{result}</pre>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)  # ⚠️ debug=True în producție
