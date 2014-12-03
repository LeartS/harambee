from datetime import date

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

    @property
    def top_reporters(self):
        res = {}
        for reporter in self.reporters:
            res[reporter] = res.get(reporter, 0) + 1
        return sorted(res.items(), key=lambda x: x[1], reverse=True)

    def serialize_preview(self):
        return {
            'id': int(self.id),
            'name': str(self.name),
            'bug_count': len(self.bugs),
            'reporters_count': len(self.top_reporters),
        }
