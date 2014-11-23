from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import flash
from harambee import app, db
from harambee.models import City

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/city/<int:city_id>/<string:city>")
def city(city_id, city):
    city = City.query.filter(City.id == city_id).first()
    return render_template('city.html', city=city)

@app.route("/city/new", methods=['GET', 'POST'])
def new_city():
    if request.method == 'GET':
        return render_template('new_city.html')
    else:
        print(request.form)
        print(request.args)
        new_city = City(name=request.form['name'], cap=request.form['cap'])
        db.session.add(new_city)
        db.session.commit()
        flash('City created correctly', category='success')
        return redirect(url_for('city', city_id=new_city.id, city=new_city))

@app.route("/bug")
def bug():
    return render_template('bug.html')
