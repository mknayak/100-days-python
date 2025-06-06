from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
from MovieDbModel import *
from models.EditMovieFormModel import *
from models.AddMovieForm import *


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
Bootstrap5(app)


# CREATE DB
db= initializeDb(app)


# CREATE TABLE
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    movies=db.session.execute(db.Select(MovieDbModel).order_by(MovieDbModel.title)).scalars().all()
    return render_template("index.html", movies=movies)

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        title = form.title.data
    return render_template('add.html',form=form)


@app.route("/update/<movie_id>", methods=["GET", "POST"])
def update(movie_id):
    movie = db.session.query(MovieDbModel).get(movie_id)
    edit_movie=EditMovieForm(rating=movie.rating,review=movie.review,id=movie.id)
    if edit_movie.validate_on_submit():
        with app.app_context():
            movie_to_update=db.session.query(MovieDbModel).get(movie.id)
            movie_to_update.rating=float(edit_movie.rating.data)
            movie_to_update.review=edit_movie.review.data
            db.session.commit()
        return redirect(url_for("home"))
    return render_template('edit.html',movie=movie,form=edit_movie)

@app.route("/delete/<movie_id>", methods=["GET"])
def delete(movie_id):
    with app.app_context():
        movie_to_delete=db.session.query(MovieDbModel).get(movie_id)
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect(url_for("home"))


@app.route("/add-s",methods=["GET","POST"])
def add_s():
    new_movie = MovieDbModel(
        title="Avatar The Way of Water",
        year=2022,
        description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
        rating=7.3,
        ranking=9,
        review="I liked the water.",
        img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    )
    with app.app_context():
        db.session.add(new_movie)
        db.session.commit()
    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
