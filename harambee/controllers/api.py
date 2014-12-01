from flask import jsonify

from harambee import app
from harambee.models import City


@app.route("/data/cities/preview")
def cities_preview():
    cities = City.query.all()
    cities = list(c.serialize_preview() for c in cities)
    return jsonify(cities=cities)
