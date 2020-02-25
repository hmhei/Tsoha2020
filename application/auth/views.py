from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, login_required
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form, 
        error = "Käyttäjätunnusta tai salasanaa ei ole olemassa")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/auth/register/", methods = ["GET", "POST"])
def auth_register():
    if request.method == "GET":
        return render_template("auth/registerform.html", form = RegisterForm())

    if request.method == "POST":
        form = RegisterForm(request.form)

        if not form.validate():
            return render_template("auth/registerform.html", form = form)

        new = User(form.name.data, form.username.data, form.password.data, False)

        db.session().add(new)
        db.session().commit()
  
        return redirect(url_for("loans_index"))

@app.route("/auth/modify/", methods = ["GET"])
@login_required(role="USER")
def auth_modify():
    user = User.query.filter_by(id = current_user.id).first()
    form = RegisterForm()

    form.name.data = user.name
    form.username.data = user.username

    return render_template("auth/modifyform.html", form=form)

@app.route("/auth/modify/", methods = ["POST"])
@login_required(role="USER")
def auth_save():
    
    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/modifyform.html", form = form)
    
    user = User.query.filter_by(id = current_user.id).first()
    
    user.name = form.name.data
    user.username = form.username.data
    user.password = form.password.data

    db.session().commit()

    return redirect(url_for("index"))