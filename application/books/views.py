from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application import app, db, login_required
from application.books.models import Book
from application.books.forms import BookForm

@app.route("/books/", methods=["GET"])
@login_required
def books_index():
    return render_template("books/list.html", books = Book.query.all())

@app.route("/books/new/")
@login_required
def books_form():
    return render_template("books/new.html", form = BookForm())

@app.route("/books/delete/<book_id>/", methods=["GET"])
@login_required(role="ADMIN")
def books_delete(book_id):

    book = Book.query.get(book_id)
    db.session().delete(book)
    db.session().commit()

    return redirect(url_for("books_index"))

@app.route("/books/", methods=["POST"])
@login_required(role="ADMIN")
def books_create():
    form = BookForm(request.form)

    if not form.validate():
        return render_template("books/new.html", form = form)

    book = Book(form.name.data)
    book.published = form.published.data
    book.account_id = current_user.id

    db.session().add(book)
    db.session().commit()
  
    return redirect(url_for("books_index"))