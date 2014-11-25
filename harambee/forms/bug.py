from flask_wtf import Form
from wtforms import StringField, TextAreaField, HiddenField

class NewBugForm(Form):
    title = StringField('Title')
    description = TextAreaField('Description')
    city_id = HiddenField('city')
