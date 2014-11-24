from flask import render_template
from flask import request
from flask import redirect, url_for
from flask import flash
from harambee import app, db
from harambee.models import City, Bug

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

@app.route("/bug/new", methods=['GET', 'POST'])
def new_bug():
    if request.method == 'GET':
        return render_template('new_bug.html')
    else:
        new_bug = Bug(
            title=request.form['title'],
            content=request.form['content'],
            city_id=request.form['city'],
        )
        db.session.add(new_bug)
        db.session.commit()
        flash('Bug created correctly', category='success')
        return redirect(url_for('bug'))

@app.route("/bug/<int:bug_id>")
@app.route("/bug/<int:bug_id>/<string:title>")
def bug(bug_id, title=None):
    bug = Bug.query.filter(Bug.id == bug_id).first()
    return render_template('bug.html', bug=bug)
