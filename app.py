# Grab our app package
from flask import Flask, render_template, url_for, redirect, jsonify
from flask_pymongo import PyMongo
from bson import json_util, ObjectId
from bson.json_util import dumps
import json
import scrape

app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/calfire")

### ROUTES ###
# Home Page Route
@app.route('/')
@app.route('/home')
def home():

    fires = mongo.db.fires.find_one()
    return render_template('index.html', data=fires)

# Scrape Route
@app.route('/scrape')
def scrape():
    # Call Scrape Method - Do Scrape Stuff Here
    return redirect("/")

# Statistics Page
@app.route('/stats')
def stats():
    return render_template('stats.html')

# About Page
@app.route('/about')
def about():
    return render_template('about.html')


### DATABASE ROUTES ### 
@app.route('/<attb>/data')
def db_data(attb):

    db_data = mongo.db.fires.find({'IsActive':attb}, {'_id': False})
    print('this route was pinged')
    parsed = [x for x in db_data]
    print('parsed: ', parsed)
    return jsonify(parsed)

@app.route('/database')
def database():
    db_data = mongo.db.fires.find()
    print('this route was pinged')
    parsed = [x for x in db_data]
    print('parsed: ', parsed)
    return jsonify(parsed)

# Debugger
if __name__ == '__main__':
    app.run(debug=True)
