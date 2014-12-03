from flask_wtf import Form
from wtforms import StringField, IntegerField

class NewCityForm(Form):
    name = StringField('Name')
    population = IntegerField('Population')
