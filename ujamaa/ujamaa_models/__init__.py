import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_uploads import UploadSet, DOCUMENTS, configure_uploads
from ujamaa_models.config import Config




db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info' 
mail = Mail()

# Configure the image uploading via Flask-Uploads
documents = UploadSet('documents', DOCUMENTS)




def create_app(config_class=Config):
	app = Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)

	configure_uploads(app, documents)

	from ujamaa_models.users.routes import users 
	from ujamaa_models.posts.routes import posts
	from ujamaa_models.main.routes import main
	from ujamaa_models.programs.routes import programs 
	from ujamaa_models.courses.routes import courses 
	from ujamaa_models.courseoutlines.routes import courseoutlines 
	from ujamaa_models.exams.routes import exams
	from ujamaa_models.notes.routes import notes
	from ujamaa_models.programs.routes import programs
	from ujamaa_models.universities.routes import universities

	app.register_blueprint(users)
	app.register_blueprint(posts)
	app.register_blueprint(main)
	app.register_blueprint(courses)
	app.register_blueprint(courseoutlines)
	app.register_blueprint(exams)
	app.register_blueprint(notes) 
	app.register_blueprint(programs)
	app.register_blueprint(universities) 

	return app

