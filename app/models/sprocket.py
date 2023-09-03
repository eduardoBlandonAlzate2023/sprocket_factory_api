from app import db

class Sprocket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teeth = db.Column(db.Integer)
    pitch_diameter = db.Column(db.Float)
    outside_diameter = db.Column(db.Float)
    pitch = db.Column(db.Float)
