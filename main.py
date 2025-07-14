from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '''
        <html>
            <head><title>Poza mea</title></head>
            <body>
                <h1>Salut! Aplicația funcționează corect!</h1>
                <img src="/static/image.jpg" alt="Imagine" width="300">
            </body>
        </html>
    '''

@app.route('/health')
def health():
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=50000, debug=False)
