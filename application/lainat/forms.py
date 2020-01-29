from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, validators

class LainaForm(FlaskForm):
    name = StringField("Kirjan nimi", [validators.Length(min=5)])
    returned = BooleanField("Palautettu")

    class Meta:
        csrf = False
