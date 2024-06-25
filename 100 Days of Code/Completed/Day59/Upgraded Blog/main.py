from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_json = requests.get("https://api.npoint.io/f46ee92a2414840734a9").json()


@app.route("/")
def home():
    return render_template("index.html", all_posts=blog_json)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:number>")
def post(number):
    requested_post = None
    for blog_post in blog_json:
        if blog_post["id"] == number:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)