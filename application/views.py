from flask import render_template
from application import app
from application.auth.models import User

@app.route("/")
def index():
    return render_template("index.html", 
    has_loans=User.list_users_with_loans_and_loans_amount())
