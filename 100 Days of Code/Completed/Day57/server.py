from flask import Flask, render_template
import random
import datetime as dt
import requests

app = Flask(__name__)

AUTHOR = "Gary Siu"


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = dt.datetime.now().year
    return render_template("index.html", num=random_number,
                           year=current_year, author=AUTHOR)


@app.route("/guess/<name>")
def guess(name):
    gender_json = requests.get(f"https://api.genderize.io?name={name}").json()
    gender = gender_json["gender"]
    age_json = requests.get(f"https://api.agify.io?name={name}").json()
    age = age_json["age"]
    return render_template("guess.html", name=name,
                           gender=gender, age=age)


@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
