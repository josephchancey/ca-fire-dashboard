from flask.helpers import locked_cached_property
from app import db
from datetime import date, datetime

# SQL Model for CalFire database
class Fires(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(100), nullable=True)
    updated = db.Column(db.DateTime, nullable=True)
    started = db.Column(db.DateTime, nullable=True)
    county = db.Column(db.String(100), nullable=True)
    location = db.Column(db.String(260), nullable=True)
    agency_names = db.Column(db.String(999), nullable=True)
    lat = db.Column(db.Float(20), nullable=True)
    long = db.Column(db.Float(20), nullable=True)
    fire_type = db.Column(db.String(100), nullable=True)
    url = db.Column(db.String(80), nullable=True)
    extinguished_date = db.Column(db.DateTime, nullable=True)
    is_active = db.Column(db.Boolean, nullable=True)
    is_calfire_incident = db.Column(db.Boolean, nullable=True)
    percent_contained = db.Column(db.Integer(3), nullable=True)
    
    def __repr__(self):
        return f"Post('{self.id}', '{self.name}, {self.updated}', '{self.is_active}')"