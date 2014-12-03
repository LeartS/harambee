from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import flash

from harambee import app, db
from harambee.models import City, User
from harambee.forms import NewCityForm


@app.route("/city/<int:city_id>/")
@app.route("/city/<int:city_id>/<string:city>")
def city(city_id, city=None):
    city = City.query.filter(City.id == city_id).first()
    users = User.query.all()
    return render_template('city.html', city=city, users=users)

@app.route("/city/new", methods=['GET', 'POST'])
def new_city():
    city_form = NewCityForm()
    if city_form.is_submitted():
        if city_form.validate():
            city = City(
                name=city_form.name.data,
                population=city_form.population.data
            )
            db.session.add(city)
            db.session.commit()
            return redirect(url_for('city', city_id=city.id))
    return render_template('new_city.html', form=city_form)
