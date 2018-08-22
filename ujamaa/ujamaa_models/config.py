import os


class Config:
	SECRET_KEY = 'a58e4aa584b5a356c5d25c8cc28c8df5'
	SQLALCHEMY_DATABASE_URI = 'postgresql://mikeproject:awesomeness@localhost/academic_resource_sharing_system'
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'mikegachunji@gmail.com'
	MAIL_PASSWORD = 'maguyz94'
	# grab the folder of the top-level directory of this project
	BASEDIR = os.path.abspath(os.path.dirname(__file__))
	TOP_LEVEL_DIR = os.path.abspath(os.curdir)
	# Uploads
	UPLOADS_DEFAULT_DEST = TOP_LEVEL_DIR + '/ujamaa_models/static/img/'
	UPLOADS_DEFAULT_URL = 'http://localhost:5000/static/img/'
	 
	UPLOADED_DOCUMENTS_DEST = TOP_LEVEL_DIR + '/ujamaa_models/static/img/'
	UPLOADED_DOCUMENTS_URL = 'http://localhost:5000/static/img/'