from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import  DataRequired,URL
class AddBookForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    author = StringField('Author',validators=[DataRequired()])
    rating = StringField('Rating',validators=[DataRequired()])
    submit = SubmitField('Submit')
