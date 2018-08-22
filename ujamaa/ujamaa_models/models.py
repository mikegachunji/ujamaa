from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from ujamaa_models import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_type = db.Column(db.String(20), nullable=False)
    university_id = db.Column(db.Integer, db.ForeignKey('university.id'))
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'))    
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)    
    posts = db.relationship('Post', backref='author', lazy=True)
    courseoutlines = db.relationship('CourseOutline', backref='author_courseoutline', lazy=True)
    exams = db.relationship('Exam', backref='author_exam', lazy=True)
    notes = db.relationship('Notes', backref='author_notes', lazy=True)


    def __init__(self, user_type, university_id, program_id, username, email, password):
        self.user_type = user_type
        self.university_id = university_id
        self.program_id = program_id
        self.username = username
        self.email = email
        self.password = password        


    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"



class University(db.Model):

    __tablename__ = "university"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    users = db.relationship('User', backref='user_university', lazy=True)

    def __init__(self, title):
        self.title = title    

    def __repr__(self):
        return f"University('{self.title}')"




class Post(db.Model):

    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'))

    def __init__(self, title, content, user_id, program_id):
        self.title = title
        self.content = content
        self.user_id = user_id
        self.program_id = program_id

    def __repr__(self):
    	return f"Post('{self.title}', '{self.date_posted}')"


class Program(db.Model):

    __tablename__ = "program"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    users = db.relationship('User', backref='user_prog', lazy=True)
    courses = db.relationship('Course', backref='course_program', lazy=True)
    courseoutlines = db.relationship('CourseOutline', backref='program_courseoutline', lazy=True)
    exams = db.relationship('Exam', backref='exam_program', lazy=True)
    notes = db.relationship('Notes', backref='notes_program', lazy=True)

    def __init__(self, title):
        self.title = title
    

    def __repr__(self):
        return f"Program('{self.title}')"


class Course(db.Model):

    __tablename__ = "course"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'))
    courseoutlines = db.relationship('CourseOutline', backref='course_outline', lazy=True)
    exams = db.relationship('Exam', backref='course_exam', lazy=True)
    notes = db.relationship('Notes', backref='course_notes', lazy=True)

    def __init__(self, title, year, program_id):
        self.title = title
        self.year = year
        self.program_id = program_id
    

    def __repr__(self):
        return f"Post('{self.title}', '{self.year}', '{self.program_id}')"


class CourseOutline(db.Model):

    __tablename__ = "courseoutline"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    document_filename = db.Column(db.String, default=None, nullable=True)
    document_url = db.Column(db.String, default=None, nullable=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'))

    def __init__(self, title, description, course_id, user_id, program_id, document_filename=None, document_url=None):
        self.title = title
        self.description = description
        self.document_filename = document_filename
        self.document_url = document_url
        self.course_id = course_id
        self.user_id = user_id
        self.program_id = program_id

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Exam(db.Model):

    __tablename__ = "exam"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'))

    def __init__(self, title, description, date_posted, content, course_id, user_id, program_id):
        self.title = title
        self.description = description
        self.date_posted = date_posted
        self.content = content
        self.course_id = course_id
        self.user_id = user_id
        self.program_id = program_id

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Notes(db.Model):

    __tablename__ = "notes"


    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    program_id = db.Column(db.Integer, db.ForeignKey('program.id'))

    def __init__(self, title, description, date_posted, content, course_id, user_id, program_id):
        self.title = title
        self.description = description
        self.date_posted = date_posted
        self.content = content
        self.course_id = course_id
        self.user_id = user_id
        self.program_id = program_id

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"









