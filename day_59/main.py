from flask import Flask, render_template
import requests

posts = requests.get("https://api.npoint.io/674f5423f73deab1e9a7").json()
print(posts)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/blog/<int:num>")
def get_blog(num):
    for post in posts:
        if post["id"] == num:
            return render_template("blog.html", post=post)
    return render_template("404.html"), 404

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)

