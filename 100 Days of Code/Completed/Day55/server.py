import random
from flask import Flask

app = Flask(__name__)

answer = random.randint(0, 9)


@app.route('/')
def home():
    return ('<h1><b>Guess a number between 0 and 9</b></h1>'
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/'
            'giphy.gif">')


@app.route('/<int:guess>')
def user_guess(guess):
    if guess < answer:
        return ('<h1 style="color=red"><b>Too low, try again!</b></h1>'
                '<img src="https://media.giphy.com/media/'
                'jD4DwBtqPXRXa/giphy.gif">')
    elif guess > answer:
        return ('<h1 style="color=blue"><b>Too high, '
                'try again!</b></h1>'
                '<img src="https://media.giphy.com/media/'
                '3o6ZtaO9BZHcOjmErm/giphy.gif">')
    else:
        return ('<h1 style="color=green"><b>You found me!</b></h1>'
                '<img src="https://media.giphy.com/media/'
                '4T7e4DmcrP9du/giphy.gif">')


if __name__ == "__main__":
    app.run(debug=True)