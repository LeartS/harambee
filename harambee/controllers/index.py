from flask import render_template
from flask import request

from harambee import app
from harambee.models import City


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    print(repr(request.args['city']))
    if not request.args['city']:
        cities = City.query.limit(10).all()
    else:
        search_query = '%{}%'.format(request.args['city'])
        cities = City.query.filter(City.name.ilike(search_query)).all()
    return render_template('search_results.html', cities=cities)
