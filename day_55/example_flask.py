from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
	return ("<p>Hello, World!</p>"
	        "<p>My name is Sergio!</p>")


@app.route("/bye")
def bye():
	return "<p>Bye Bye</p>"

@app.route("/<name>")
def greet(name):
	return f"Hello {escape(name+'12')}!"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
@app.route('/login')
def login():
    return 'login'

@app.route('/profile/<username>')
def profile(username):
    return f'{username}\'s profile'

if __name__ == "__main__":
    # with app.test_request_context():
    #     print(url_for('hello_world'))
    #     print(url_for('login'))
    #     print(url_for('login', next='/'))
    #     print(url_for('profile', username='John Doe'))

    app.run(debug=True)
