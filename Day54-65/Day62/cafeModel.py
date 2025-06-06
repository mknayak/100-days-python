from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,SelectField
from wtforms.validators import  DataRequired,URL
class Cafe(FlaskForm):
    name = StringField('What is your cafe name?', validators=[DataRequired()])
    location = StringField('Cafe Location?', validators=[URL()])
    opening_time = StringField('Cafe Opening Time?', validators=[DataRequired()])
    closing_time = StringField('Cafe Closing Time?', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating?',
                                choices=[('☕'),('☕☕'),('☕☕☕'),('☕☕☕☕'),('☕☕☕☕☕')],
                                validators=[DataRequired()])
    wifi_strength_rating= SelectField('Wifi Strength Rating?',
                                choices=[('💪'),('💪💪'),('💪💪💪'),('💪💪💪💪'),('💪💪💪💪💪')],
                                validators=[DataRequired()])
    power_socket_availability= SelectField('Power Socket Availability?',
                                choices=[('🔌'),('🔌🔌'),('🔌🔌🔌'),('🔌🔌🔌🔌'),('🔌🔌🔌🔌🔌')],
                                           validators=[DataRequired()])
    add_button = SubmitField('Add Cafe')