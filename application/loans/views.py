from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.loans.models import Loan
from application.loans.forms import LoanForm

@app.route("/loans/", methods=["GET"])
@login_required
def loans_index():
    return render_template("loans/list.html", loans = Loan.query.all())

@app.route("/loans/new/")
@login_required
def loans_form():
    return render_template("loans/new.html", form = LoanForm())
  
@app.route("/loans/<loan_id>/", methods=["POST"])
@login_required
def loans_set_done(loan_id):

    l = Loan.query.get(loan_id)
    l.done = True
    db.session().commit()

    return redirect(url_for("loans_index"))

@app.route("/delete/<loan_id>/", methods=["GET"])
@login_required
def loans_delete(loan_id):

    l = Loan.query.get(loan_id)
    db.session().delete(l)
    db.session().commit()

    return redirect(url_for("loans_index"))

@app.route("/loans/", methods=["POST"])
@login_required
def loans_create():
    form = LoanForm(request.form)

    if not form.validate():
        return render_template("loans/new.html", form = form)

    l = Loan(form.name.data)
    l.done = form.returned.data
    l.account_id = current_user.id

    db.session().add(l)
    db.session().commit()
  
    return redirect(url_for("loans_index"))
