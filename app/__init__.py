from flask import Flask
from flask_pymongo import PyMongo
import json
# from config import SECRET_KEY

app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/calfire"
mongo = PyMongo(app)

# Call routes last because routes depends on db declaired above
from app import routes