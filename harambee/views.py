from flask import render_template
from flask import request
from flask import redirect, url_for
from harambee import app
from harambee.models import City

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/city/<string:city>")
def city(city):
    city = City.query.filter(City.name == city).first()
    return render_template('city.html', city=city)

@app.route("/city/new", methods=['GET', 'POST'])
def new_city():
    if request.method == 'GET':
        return render_template('new_city.html')
    else:
        print(request.form)
        print(request.args)
        new_city = City(name=request.form['name'], cap=request.form['cap'])
        return redirect(url_for('city', city=new_city))

@app.route("/bug")
def bug():
    return render_template('bug.html')
