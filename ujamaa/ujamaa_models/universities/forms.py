from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class UniversityForm(FlaskForm):
	title = StringField('Name of University', validators=[DataRequired()])
	submit = SubmitField('Post')