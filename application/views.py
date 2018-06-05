from flask import render_template, request, url_for, redirect

from flask_login import login_required, current_user

from application import app, db 
from application.drinks.models import Drink
from application.drinks.forms import DrinkForm

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/drinks", methods=["GET"])
def drinks_index():
	return render_template("drinks/list.html", drinks = Drink.query.all())

@app.route("/drinks/new/")
@login_required
def drinks_form():
   	 return render_template("drinks/new.html", form = DrinkForm())

@app.route("/drinks/", methods=["POST"])
@login_required
def drinks_create():
	form = DrinkForm(request.form)

	if not form.validate():
        	return render_template("drinks/new.html", form = form)

	d = Drink(form.name.data)
	d.account_id = current_user.id

	db.session().add(d)
	db.session().commit()
  
	return redirect(url_for("drinks_index"))
