import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    SQLALCHEMY_DATABASE_URI = 'postgres://ychsrgngohrftl:84f0d0038ef2355d8f53357754f892f6578c880427dbc8336d22f45904500f58@ec2-54-235-108-217.compute-1.amazonaws.com:5432/d9mt849lffqr5t'
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
    UPLOAD_FOLDER = "./uploads"
class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False