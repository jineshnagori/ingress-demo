from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <h1>Hello World</h1>
    <p>Click the links below:</p>
    <a href="/node-app">Node App</a>
    <a href="/web-app">Web App</a>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0')