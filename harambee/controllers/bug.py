from flask import render_template
from flask import redirect, url_for

from harambee import app, db
from harambee.models import Bug
from harambee.forms import NewBugForm


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
