from flask_wtf import FlaskForm
from flask_wtf import Form
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed, FileRequired
from ujamaa_models import documents

class AddCourseOutlineForm(Form):
    title = StringField('Course Outline Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    document = FileField('Document', validators=[FileRequired(), FileAllowed(documents, 'Documents only!')])