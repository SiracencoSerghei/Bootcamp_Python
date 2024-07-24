from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)

##CREATE DATABASE
class Base(DeclarativeBase):
    pass

basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)
db_path = os.path.join(basedir, 'new-books-collection.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


##CREATE TABLE
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()
   
def create_new_record(title, author, rating):
    with app.app_context():
        new_book = Book(title=title, author=author, rating=rating)
        db.session.add(new_book)
        db.session.commit()
        
def read_all_books():
    with app.app_context():
        all_books = Book.query.all()
        return all_books

@app.route('/')
def home():
	return render_template('index.html', books=read_all_books())


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        rating = request.form["rating"]
        create_new_record(title=title, author=author, rating=rating)
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
	app.run(debug=True)
