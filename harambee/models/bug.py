from datetime import date, datetime

from harambee import app, db


class Bug(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    address = db.Column(db.String(256), )
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'), nullable=False)
    reporter_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                            nullable=False, default=1)
    report_date = db.Column(db.Date, default=lambda: date.today())
    update_datetime = db.Column(db.DateTime, default=lambda: datetime.now(),
                            onupdate=lambda: datetime.now())
