from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, DATE
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import requests
import os
import dotenv

dotenv.load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))
SECRET = os.environ.get("PASSWD")
MOVIE_SEARCH_URL = os.environ.get("TMDB_SEARCH_URL")
MOVIE_DB_API_KEY = os.environ.get("TMDB_API_KEY")
MOVIE_DB_INFO_URL = os.environ.get("TMDB_INFO_URL")
MOVIE_DB_IMAGE_URL = os.environ.get("TMDB_IMAGE_URL")

app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass
db_path = os.path.join(basedir, "my_top_10_movies.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{db_path}'

db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int]  = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    
class EditForm(FlaskForm):
    rating = StringField(label='Your Rating out of 10 e.g. 7.5', validators=[DataRequired(), ])
    review = StringField(label='Your Review', validators=[DataRequired(), Length(min=1, max=75)])
    submit = SubmitField(label='Done')
    
class FindMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")
    
with app.app_context():
    db.create_all()
    
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#     second_movie = Movie(
#         title="Avatar The Way of Water",
#         year=2022,
#         description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#         rating=7.3,
#         ranking=9,
#         review="I liked the water.",
#         img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
#     )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()

def get_all_movies():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating.desc()))
    all_movies = result.scalars().all()
    
    for i, movie in enumerate(all_movies):
        movie.ranking = i + 1
    
    db.session.commit()
    return all_movies

@app.route("/")
def home():
    all_movies = get_all_movies()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["GET", "POST"])
def add():
    form = FindMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(MOVIE_SEARCH_URL, params = {"api_key": MOVIE_DB_API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template("select.html", options = data)
    return render_template("add.html", form = form)

@app.route('/edit',methods=["GET", "POST"])
def edit():
    form = EditForm()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie,movie_id)
    if form.validate_on_submit():
        try:
            movie.rating = float(form.rating.data)
        except ValueError:
            movie.rating = movie.rating
        finally:
            movie.review = form.review.data
            db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit.html',movie=movie,form=form)

@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        response = requests.get(movie_api_url, params={"api_key":MOVIE_DB_API_KEY, "language":"en-US"})
        data = response.json()
        new_movie = Movie(
            title = data["title"],
            year = data["release_date"].split("-")[0],
            img_url = f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description = data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)
