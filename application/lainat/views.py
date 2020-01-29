from application import app, db
from flask import redirect, render_template, request, url_for
from application.lainat.models import Laina
from application.lainat.forms import LainaForm

@app.route("/lainat", methods=["GET"])
def lainat_index():
    return render_template("lainat/list.html", lainat = Laina.query.all())

@app.route("/lainat/new/")
def lainat_form():
    return render_template("lainat/new.html", form = LainaForm())
  
@app.route("/lainat/<laina_id>/", methods=["POST"])
def lainat_set_done(laina_id):

    l = Laina.query.get(laina_id)
    l.done = True
    db.session().commit()
  
    return redirect(url_for("lainat_index"))

@app.route("/lainat/", methods=["POST"])
def lainat_create():
    form = LainaForm(request.form)

    if not form.validate():
        return render_template("lainat/new.html", form = form)

    l = Laina(form.name.data)
    l.done = form.returned.data

    db.session().add(l)
    db.session().commit()
  
    return redirect(url_for("lainat_index"))
