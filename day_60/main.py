from flask import Flask, render_template, request
import requests
import smtplib
import os
import dotenv

dotenv.load_dotenv()
OWN_EMAIL = os.environ.get("MY_EMAIL")
OWN_PASSWORD = os.environ.get("MY_EMAIL_PASSWORD")

posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
# print(posts)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/blog/<int:num>")
def get_blog(num):
    for post in posts:
        if post["id"] == num:
            return render_template("blog.html", post=post)
    return render_template("404.html"), 404

# @app.route("/contact")
# def contact():
#     return render_template("contact.html")
#
# @app.route("/form-entry")
# def receive_data():
#     if request.method == "POST":
#         name = request.form["name"]
#         email = request.form["email"]
#         phone = request.form["phone"]
#         message = request.form["message"]
#         # Render the response template with the submitted data
#         return render_template("form_response.html", name=name, email=email, phone=phone, message=message)

# @app.route("/contact", methods=["GET", "POST"])
# def contact():
#     if request.method == "POST":
#         data = request.form
#         print(data["name"])
#         print(data["email"])
#         print(data["phone"])
#         print(data["message"])
#         return "<h1>Successfully sent your message</h1>"
#     return render_template("contact.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    print(email_message)
    conection = smtplib.SMTP("smtp.gmail.com", 587)
    with conection as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


if __name__ == "__main__":
    app.run(debug=True)

