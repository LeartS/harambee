from datetime import date

from harambee import app, db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    registration_date = db.Column(db.Date, default=lambda: date.today())
    bugs = db.relationship('Bug', backref='reporter', collection_class=set)
