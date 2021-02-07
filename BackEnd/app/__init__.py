from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand



"""User show side Initialization file which connect all touched files app 
    All config for app side we write in init file
"""
# Create object app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['UPLOAD_PATH']= "app/static/upload"
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# dot(.) => mean that, we want to import from route file for __init__.py
from . import routes
from . import forms
from . import models

import admin
import blog
import auth




