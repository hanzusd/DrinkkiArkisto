from flask import Flask
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class RegisterForm(FlaskForm):
    name = StringField("Nimi")
    username = StringField("Käyttäjätunnus")
    password = PasswordField("Salasana", [
        validators.DataRequired(),
        validators.EqualTo('passwordCheck', message='Salasanat eivät ole samat')])
    passwordCheck = PasswordField("Salasana uudestaan")
  
    class Meta:
        csrf = False

