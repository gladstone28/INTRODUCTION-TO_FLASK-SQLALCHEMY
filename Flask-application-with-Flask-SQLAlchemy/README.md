link to lesson:

https://www.codecademy.com/courses/learn-flask-databases/lessons/flask-intro-sql-alchemy/exercises/flask-sqlalchemy


INTRODUCTION TO FLASK-SQLALCHEMY
Flask application with Flask-SQLAlchemy
2 min
Flask-SQLAlchemy is an extension for Flask that supports the use of a Python SQL Toolkit called SQLAlchemy.

To start creating a minimal application, in addition to importing Flask, we also need to import SQLAlchemy class from the flask_sqlalchemy module:

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

The next step is to create our Flask app instance:

app = Flask(__name__)

To enable communication with a database, the Flask-SQLAlchemy extension takes the location of the application’s database from the SQLALCHEMY_DATABASE_URI configuration variable we set in the following way:

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db' 

Next, we set the SQLALCHEMY_TRACK_MODIFICATIONS configuration option to False to disable a feature of Flask-SQLAlchemy that signals the application every time a change is about to be made in the database.

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Finally, we create an SQLAlchemy object and bind it to our app:

db = SQLAlchemy(app)
