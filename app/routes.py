# Import dependencies
from flask import render_template, url_for, redirect
from app import app

### ROUTES ###
# Home Page Route
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

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
