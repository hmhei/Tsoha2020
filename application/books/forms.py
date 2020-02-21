from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, validators

class BookForm(FlaskForm):
    name = StringField("Nimi", [validators.Length(min=5, max=30)])
    author = StringField("Kirjailija", [validators.Length(min=5, max=30)])
    published = IntegerField("Julkaisuvuosi", [validators.NumberRange(min=1800, max=2020)])
    count = IntegerField("Lukumäärä", [validators.NumberRange(min=1, max=10)])

    class Meta:
        csrf = False
