from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class ProgramForm(FlaskForm):
	title = StringField('Name of Program', validators=[DataRequired()])
	submit = SubmitField('Post')