from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from config import SECRET_KEY

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# SQLAlchemy database instance creation - Ready to work with database
db = SQLAlchemy(app)

# Call routes last because routes depends on db declaired above
from app import routes