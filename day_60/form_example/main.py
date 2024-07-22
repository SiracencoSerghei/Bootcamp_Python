from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def index():
	return render_template('index.html')

@app.post("/login")
def receive_data():
	error = None
	if request.method == 'POST':
		print("💪 Success! Form submitted")
		username = request.form.get('username')
		password = request.form.get('password')
		return f"Received: Username - {username}, Password - {password}"




if __name__ == "__main__":
	app.run(debug=True)
	