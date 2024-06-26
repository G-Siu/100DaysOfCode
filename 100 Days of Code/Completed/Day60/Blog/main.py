from flask import Flask, render_template, request
import requests
from smtplib import SMTP

USERNAME = ""
PASSWORD = ""

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/f46ee92a2414840734a9").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        update = "Successfully sent your message"
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", update=update)
    return render_template("contact.html")


def send_email(name, email, phone, message):
    email_message = (f"Subject: New Message\n\n"
                     f"Name: {name}\n"
                     f"Email: {email}\n"
                     f"Phone: {phone}\n"
                     f"Message: {message}")
    with SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(USERNAME, PASSWORD)
        conn.sendmail(USERNAME, USERNAME, email_message)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
