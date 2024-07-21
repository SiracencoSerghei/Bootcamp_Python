
from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    current_year = datetime.datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data["gender"]
    age_url = f"https://api.agify.io?name={name}"
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", person_name=name, gender=gender, age=age)


@app.route("/blogs")
def get_blogs():
    blog_url = "https://api.npoint.io/03a5af93f91ac9b1f073"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blogs.html", posts=all_posts)

@app.route("/blog/<int:num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/03a5af93f91ac9b1f073"
    response = requests.get(blog_url)
    all_posts = response.json()
    for post in all_posts:
        if post["id"] == num:
            return render_template("blog.html", post=post)
    return render_template("404.html"), 404

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)


