##CREATE DATABASE
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    pass

def initializeDb(app):
    # Create the extension
    db = SQLAlchemy(model_class=Base)
    # Initialise the app with the extension
    db.init_app(app)
    return db

class MovieDbModel(Base):
    __tablename__ = 'movies'
    id : Mapped[int] = mapped_column(Integer, primary_key=True,autoincrement=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer)
    description: Mapped[str] = mapped_column(String(250))
    rating: Mapped[float]  = mapped_column(Float)
    ranking: Mapped[int]  = mapped_column(Integer)
    review: Mapped[str] = mapped_column(String(250))
    img_url: Mapped[str] = mapped_column(String(250))

    def __repr__(self):
        return f'<Movie {self.title}>'



