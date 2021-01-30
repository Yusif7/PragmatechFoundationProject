from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField,TextAreaField


class ContactForms(FlaskForm):
    name = StringField('Name')
    surname = StringField('Surname')
    submit = SubmitField()