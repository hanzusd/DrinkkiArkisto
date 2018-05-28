from flask import render_template, request, url_for, redirect
from application import app, db 
from application.drinks.models import Drink

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/drinks", methods=["GET"])
def drinks_index():
	return render_template("drinks/list.html", drinks = Drink.query.all())

@app.route("/drinks/new/")
def drinks_form():
   	 return render_template("drinks/new.html")

@app.route("/drinks/", methods=["POST"])
def drinks_create():
	d = Drink(request.form.get("name"))

	db.session().add(d)
	db.session().commit()
  
	return redirect(url_for("drinks_index"))
