from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <form action="/greet" method="post">
            <input type="text" name="name" placeholder="Enter your name" required>
            <input type="submit" value="Greet Me">
        </form>
    '''

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name')
    return f'<h1>Hello, {name}! Welcome to Tech Review.</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
