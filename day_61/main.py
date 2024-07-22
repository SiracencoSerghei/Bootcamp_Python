from flask import Flask, render_template, flash
from flask_wtf import  FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import os
import dotenv
from flask_bootstrap import Bootstrap5 # pip install bootstrap-flask

dotenv.load_dotenv()

SECRET = os.environ.get("PASSWD")

class MyForm(FlaskForm):
    name = StringField(label='Username', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Log In')


app = Flask(__name__)
app.secret_key = SECRET
bootstrap = Bootstrap5(app) # initialise bootstrap-flask 


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        if email == "admin@email.com" and password == "12345678" :
            return render_template('success.html')
        return render_template('denied.html')
    return render_template("login.html", form=form)



if __name__ == '__main__':
    app.run(debug=True)
