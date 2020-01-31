from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.lainat.models import Laina
from application.lainat.forms import LainaForm

@app.route("/lainat/", methods=["GET"])
@login_required
def lainat_index():
    return render_template("lainat/list.html", lainat = Laina.query.all())

@app.route("/lainat/new/")
@login_required
def lainat_form():
    return render_template("lainat/new.html", form = LainaForm())
  
@app.route("/lainat/<laina_id>/", methods=["POST"])
@login_required
def lainat_set_done(laina_id):

    l = Laina.query.get(laina_id)
    l.done = True
    db.session().commit()
  
    return redirect(url_for("lainat_index"))

@app.route("/lainat/", methods=["POST"])
@login_required
def lainat_create():
    form = LainaForm(request.form)

    if not form.validate():
        return render_template("lainat/new.html", form = form)

    l = Laina(form.name.data)
    l.done = form.returned.data
    l.account_id = current_user.id

    db.session().add(l)
    db.session().commit()
  
    return redirect(url_for("lainat_index"))
