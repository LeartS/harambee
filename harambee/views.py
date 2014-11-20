from flask import render_template
from harambee import app

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/<string:city>")
def city(city):
    return render_template('city.html', city=city)

@app.route("/bug")
def bug():
    return render_template('bug.html')
