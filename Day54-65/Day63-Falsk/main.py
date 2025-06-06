from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import CSRFProtect
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
from AddBook import  AddBookForm

##CREATE DATABASE
class Base(DeclarativeBase):
    pass

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///books-collection.db"
csrf = CSRFProtect(app)
all_books = []
# Create the extension
db = SQLAlchemy(model_class=Base)
# Initialise the app with the extension
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'

with app.app_context():
    db.create_all()

@app.route('/')
def home():
     result = db.session.execute(db.select(Book).order_by(Book.id))
     books=result.scalars().all()
     return render_template("index.html" ,books=books)


@app.route("/add", methods=["POST","GET"])
def add():
    model=AddBookForm()
    if model.validate_on_submit():
        with app.app_context():
            new_book = Book(title=model.title.data, author=model.author.data, rating=model.rating.data)
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('home'))

    return render_template("add.html", form=model)


if __name__ == "__main__":
    app.run(debug=True)

