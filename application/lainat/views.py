from application import app, db
from flask import redirect, render_template, request, url_for
from application.lainat.models import Laina

@app.route("/lainat", methods=["GET"])
def lainat_index():
    return render_template("lainat/list.html", lainat = Laina.query.all())

@app.route("/lainat/new/")
def lainat_form():
    return render_template("lainat/new.html")
  
@app.route("/lainat/<laina_id>/", methods=["POST"])
def lainat_set_done(laina_id):

    l = Laina.query.get(laina_id)
    l.done = True
    db.session().commit()
  
    return redirect(url_for("lainat_index"))

@app.route("/lainat/", methods=["POST"])
def lainat_create():
    t = Laina(request.form.get("name"))

    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("lainat_index"))
