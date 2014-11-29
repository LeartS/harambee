from datetime import date, datetime
from sqlalchemy.ext.associationproxy import association_proxy

from harambee import app, db

class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    population = db.Column(db.Integer, nullable=False)
    activation_date = db.Column(db.Date, default=lambda: date.today())
    bugs = db.relationship('Bug', backref=db.backref('city'),
                           collection_class=set)
    reporters = association_proxy('bugs', 'reporter')

    def __repr__(self):
        return "{}".format(self.name)

    def serialize_preview(self):
        return {
            'id': int(self.id),
            'name': str(self.name),
            'bug_count': len(self.bugs),
        }

class Bug(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(256), )
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    reporter_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    report_date = db.Column(db.Date, default=lambda: date.today())
    update_datetime = db.Column(db.DateTime, default=lambda: datetime.now(),
                            onupdate=lambda: datetime.now())

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    registration_date = db.Column(db.Date, default=lambda: date.today())
    bugs = db.relationship('Bug', backref='reporter', collection_class=set)
