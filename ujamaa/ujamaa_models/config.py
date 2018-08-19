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