from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask is working on Render!"

if __name__ == '__main__':
    app.run()
