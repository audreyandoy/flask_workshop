# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

import os
from flask import Flask


def create_app():
    '''Create an app by initializing components'''
    app = Flask(__name__)

    # Do it!
    return app

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///workshop'

# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))

# class Food(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))
#     description = db.Column(db.String(128))

# @app.route('/')
# def hello():
#     return "Hello World!"

# @app.route('/<name>/')
# def hello_name(name):
#     return "Hello {}!".format(name)
