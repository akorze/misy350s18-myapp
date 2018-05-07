from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    import random
    greeting_list = ['Ciao', 'Hei', 'Salut', 'Hola', 'Nihao']
    return random.choice(greeting_list)


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/users/<string:username>')
def users(username):
    return render_template('users.html', username=username)


if __name__ =='__main__':
    app.run()
