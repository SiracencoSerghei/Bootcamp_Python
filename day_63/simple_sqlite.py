from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# ==================
db = sqlite3.connect("book-collection.db")
cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(2, 'Cormoran', 'J. K. Rowling', '9.3')")
# db.commit()
# ==================

app = Flask(__name__)

all_books = [
	#     {"title": "Book One", "author": "Author One", "rating": 4.5},
	#     {"title": "Book Two", "author": "Author Two", "rating": 3.8},
	#     {"title": "Book Three", "author": "Author Three", "rating": 4.2},
]


@app.route('/')
def home():
	return render_template('index.html', books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
	if request.method == "POST":
		new_book = {
			"title": request.form["title"],
			"author": request.form["author"],
			"rating": request.form["rating"]
		}
		all_books.append(new_book)
		return redirect(url_for('home'))
	return render_template('add.html')


if __name__ == "__main__":
	app.run(debug=True)

