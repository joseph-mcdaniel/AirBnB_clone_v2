#!/usr/bin/python3
from flask import Flask, render_template
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def pythonfun(text="is cool"):
    return('Python {:s}'.format(text.replace('_', ' '), text=text))


@app.route('/number/<int:n>')
def number(n):
    return ('{} is a number'.format(n))


@app.route('/number_template/')
@app.route('/number_template/<int:n>')
def template(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
