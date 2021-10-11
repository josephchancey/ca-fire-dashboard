# Import dependencies
from flask import render_template, url_for
from app import app

### ROUTES ###
# Home Page Route
@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

# # About Page Route
# @app.route('/about')
# def about():
#     return render_template('about.html', title='About')
