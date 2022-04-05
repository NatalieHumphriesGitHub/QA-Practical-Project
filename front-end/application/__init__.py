from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root:{getenv('MYSQL_ROOT_PASSWORD')}@mysql:3306/games_db"
db = SQLAlchemy(app)

from application import routes
