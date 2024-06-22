from flask import Flask

app = Flask(__name__)


@app.route('/')  # / denotes home page
def hello_world():
    return "Hello, World!"

# Use 'python -m flask --app hello run' in terminal


if __name__ == "__main__":
    app.run()
