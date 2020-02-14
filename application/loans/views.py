from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required, login_manager
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
def loans_set_returned(loan_id):

    loan = Loan.query.get(loan_id)
    
    if loan.account_id != current_user.id:
        return login_manager.unauthorized()
    
    loan.returned = True
    db.session().commit()

    return redirect(url_for("loans_index"))

@app.route("/loans/delete/<loan_id>/", methods=["GET"])
@login_required
def loans_delete(loan_id):

    loan = Loan.query.get(loan_id)

    if loan.account_id != current_user.id:
        return login_manager.unauthorized()

    db.session().delete(loan)
    db.session().commit()

    return redirect(url_for("loans_index"))

@app.route("/loans/", methods=["POST"])
@login_required
def loans_create():
    form = LoanForm(request.form)

    if not form.validate():
        return render_template("loans/new.html", form = form)

    loan = Loan(form.name.data)
    loan.returned = form.returned.data
    loan.account_id = current_user.id

    db.session().add(loan)
    db.session().commit()
  
    return redirect(url_for("loans_index"))
