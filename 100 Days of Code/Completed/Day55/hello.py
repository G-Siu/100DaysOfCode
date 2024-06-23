from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route('/')  # / denotes home page
def hello_world():
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p>This is a paragraph.</p>'
            '<img src="https://media.giphy.com/media/4kbyKfgUIzI4M/'
            'giphy.gif?cid=ecf05e470mk37uj7vma91evp0q4p9t8xk3xiw7elpsan1uft'
            '&ep=v1_gifs_search&rid=giphy.gif&ct=g" width=200>')


# Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"
# Use 'python -m flask --app hello run' in terminal


if __name__ == "__main__":
    app.run(debug=True)
