from flask import Flask, request,flash
from appPackage.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

# TEMPLATE_DIR = os.path.abspath('../templates')
# STATIC_DIR = os.path.abspath('../static')

# # app = Flask(__name__) # to make the app run without any
# app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from appPackage import routes, models