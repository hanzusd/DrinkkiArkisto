from flask import render_template, request, redirect, url_for

from application import app, db
from application.auth.models import User
from application.register.forms import RegisterForm

@app.route("/register", methods=["GET", "POST"])
def register():
	form = RegisterForm(request.form)

	if request.method == 'POST' and form.validate():
		user = User(form.name.data,
			form.username.data,
			form.password.data)
		db.session().add(user)
		db.session().commit()
		return redirect(url_for("index"))
	
	return render_template("register/register.html", form=form)
