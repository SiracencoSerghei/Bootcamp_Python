from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os
import dotenv

dotenv.load_dotenv()

SECRET = os.environ.get("PASSWD")
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, "instance/users.db")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB with the UserMixin
class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()
    
login_manager = LoginManager()
login_manager.init_app(app)

# Create a user_loader callback
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)

@app.route('/')
def home():
    
    return render_template("index.html", logged_in = current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form.get("email")
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        
        if user:
            flash("You've already signed up with this email, log in instead!")
            return redirect(url_for("login"))
        
        hashed_and_salted_password = generate_password_hash(
            password=request.form.get("password"),
            method="pbkdf2:sha256",
            salt_length=16
        )
        new_user = User(
            email = request.form.get("email"),
            name = request.form.get("name"),
            password = hashed_and_salted_password,
        )
        db.session.add(new_user)
        db.session.commit()
        # log in and authenticate user after adding details to db
        load_user(new_user)
        # return redirect(url_for("secrets", name=request.form.get("name")))
        return redirect(url_for("secrets"))
    return render_template("register.html", logged_in = current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        
        if not user:
            flash("You password or email is incorrect, please try again.")
            return redirect(url_for('login'))
        
        elif not check_password_hash(user.password, password):
            flash("You password or email is incorrect, please try again.")
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for("secrets"))
        
    return render_template("login.html", logged_in = current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/download')
@login_required
def download():
   return send_from_directory("static", path="files/cheat_sheet.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
