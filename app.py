# Import dependencies
from flask import Flask, render_template, url_for, redirect, jsonify
from flask_pymongo import PyMongo
import json
import pymongo
from pymongo.common import partition_node
from scrape import scrapeData

app = Flask(__name__)

# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/calfire")

### ROUTES ###
# Home Page Route
@app.route('/')
@app.route('/home')
def home():

    return render_template('index.html')

# Scrape Route for scrape.py function
@app.route('/scrape', methods=['GET', 'POST'])
def scrape():

    scraped_data = scrapeData()
    for i in scraped_data:
        mongo.db.fires.replace_one({'_id': i['_id']}, i, upsert=True)

    return redirect("/")

# Statistics Page
@app.route('/stats')
def stats():

    return render_template('stats.html')

# About Page
@app.route('/about')
def about():
    
    return render_template('about.html')

# This route is not working, commenting out to investigate. The two routes below are an alternative implementation.
@app.route('/<attb>/active')
def db_data(attb:bool):

    if str(attb) == "true" or str(attb) =="True" or str(attb) == 1:
        db_data = list(mongo.db.fires.find({'IsActive': True}, {'_id': False}))
        print('this route True value was pinged')

    elif str(attb) == "false" or "False" or 0:
        db_data = list(mongo.db.fires.find({'IsActive': False}, {'_id': False}))
        print('this route False value was pinged')

    else:
        print("Not a Valid URL")
        return

    parsed = [x for x in db_data]

    # print('parsed: ', parsed)
    # print(type(parsed))
    return jsonify(parsed)

@app.route('/active/fires')
def activeFires():

    db_data = list(mongo.db.fires.find({'IsActive': True}, {'_id': False}))
    parsed = [x for x in db_data]
    return jsonify(parsed)
    
@app.route('/inactive/fires')
def inactiveFires():

    db_data = list(mongo.db.fires.find({'IsActive': False}, {'_id': False}))
    parsed = [x for x in db_data]
    return jsonify(parsed)


# Debugger
if __name__ == '__main__':
    app.run(debug=True)
