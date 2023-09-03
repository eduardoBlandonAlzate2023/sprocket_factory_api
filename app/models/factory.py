from app import db

class Factory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chart_data = db.Column(db.JSON)
