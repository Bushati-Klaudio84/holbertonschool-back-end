#!/usr/bin/python3


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_route():
    """Function that returns a string when / route is requested"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """Function that returns a string when /hbnb route is requested"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_print(text):
    """Function that returns a string when /c/<text> route is requested"""
    text = text.replace('_', ' ')
    return "C {}".format(text)

@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """Function that returns a string when /python/(<text>) route is requested"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)

@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Function that returns a string when /number/<n> route is requested if n is an integer"""
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Function that returns a HTML page when /number_template/<n> route is requested if n is an integer"""
    return render_template('number.html', n=n)

@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """Function that returns a HTML page indicating whether n is even or odd when /number_odd_or_even/<n> route is requested"""
    parity = "even" if n % 2 == 0 else "odd"
    return render_template('number_odd_or_even.html', n=n, parity=parity)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
