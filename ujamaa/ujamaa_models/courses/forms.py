from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class CourseForm(FlaskForm):
	title = StringField('Course Title', validators=[DataRequired()])
	year = IntegerField('Year of Study', validators=[DataRequired()])
	submit = SubmitField('Post')