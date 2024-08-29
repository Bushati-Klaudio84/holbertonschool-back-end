from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """ Function that returns a string when / route is requested """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ Function that returns a string when / route is requested """
    return ' HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def c_print(text):
    """ Function <that returns a string when / route is requested> """
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)