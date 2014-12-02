from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import flash

from harambee import app, db
from harambee.models import City, User


@app.route("/city/<int:city_id>/")
@app.route("/city/<int:city_id>/<string:city>")
def city(city_id, city=None):
    city = City.query.filter(City.id == city_id).first()
    users = User.query.all()
    return render_template('city.html', city=city, users=users)

@app.route("/city/new", methods=['GET', 'POST'])
def new_city():
    if request.method == 'GET':
        return render_template('new_city.html')
    else:
        new_city = City(name=request.form['name'], cap=request.form['cap'])
        db.session.add(new_city)
        db.session.commit()
        flash('City created correctly', category='success')
        return redirect(url_for('city', city_id=new_city.id, city=new_city))