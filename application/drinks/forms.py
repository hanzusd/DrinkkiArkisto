from flask_wtf import FlaskForm
from wtforms import StringField, validators

class DrinkForm(FlaskForm):
    name = StringField("Drinkin nimi", [validators.Length(min=3)])
  
    class Meta:
        csrf = False
