from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import flash
from flask import jsonify
from harambee import app, db
from harambee.models import City, Bug
from harambee.forms import NewBugForm

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/city/<int:city_id>/")
@app.route("/city/<int:city_id>/<string:city>")
def city(city_id, city=None):
    city = City.query.filter(City.id == city_id).first()
    return render_template('city.html', city=city)

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

@app.route("/data/cities/preview")
def cities_preview():
    cities = City.query.all()
    a = list(c.serialize_preview() for c in cities)
    print(a)
    print(type(a[0]['name']))
    return jsonify({'objects': cities})

@app.route("/city/<int:city_id>/bug/new", methods=['GET', 'POST'])
def new_bug(city_id):
    bug_form = NewBugForm(city_id=city_id)
    if bug_form.is_submitted():
        if bug_form.validate():
            bug = Bug(
                title=bug_form.title.data,
                content=bug_form.description.data,
                city_id=bug_form.city_id.data
            )
            db.session.add(bug)
            db.session.commit()
            return redirect(url_for('bug', bug_id=bug.id))
    return render_template('new_bug.html', city_id=city_id, form=bug_form)

@app.route("/bug/<int:bug_id>")
@app.route("/bug/<int:bug_id>/<string:title>")
def bug(bug_id, title=None):
    bug = Bug.query.filter(Bug.id == bug_id).first()
    return render_template('bug.html', bug=bug)
