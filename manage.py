from flask import Flask
from Flask-SQLAlchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand

from app import app
from app import db

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()