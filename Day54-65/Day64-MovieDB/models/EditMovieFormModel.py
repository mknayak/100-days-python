from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import DataRequired


class EditMovieForm(FlaskForm):
    id = HiddenField("movie_id", validators=[DataRequired()])
    rating = DecimalField('Title', validators=[DataRequired()])
    review = TextAreaField('Review', validators=[DataRequired()])
    submit = SubmitField('Submit')