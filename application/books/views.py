from flask import redirect, render_template, request, url_for
from flask_login import current_user
import datetime

from application import app, db, login_required
from application.books.models import Book
from application.books.forms import BookForm
from application.loans.models import Loan
from application.authors.models import Author

@app.route("/books/", methods=["GET"])
@login_required
def books_index():
    return render_template("books/list.html", 
    books = Book.query.all())

@app.route("/books/info/<book_id>", methods=["GET"])
@login_required
def books_info(book_id):
    return render_template("books/info.html",
    list_authors=Book.list_authors(book_id),
    book = Book.query.get(book_id))

@app.route("/books/modify/<book_id>", methods=["GET"])
@login_required
def books_modify(book_id):
    
    book = Book.query.get(book_id)
    author = Author.query.get(book_id)
    form = BookForm()
    form.name.data = book.name
    form.author.data = author.name
    form.published.data = book.published
    form.count.data = book.count
    form.desc.data = book.desc
    
    return render_template("books/new.html", form=form, num=book_id)

@app.route("/books/modify/<book_id>", methods=["POST"])
@login_required(role="ADMIN")
def books_save(book_id):

    form = BookForm(request.form)

    if not form.validate():
        return render_template("books/new.html", form=form, num=book_id)
    
    book = Book.query.get(book_id)
    author = Author.query.get(book_id)
    
    author.name = form.author.data
    book.name = form.name.data
    book.published = form.published.data
    book.count = form.count.data
    book.desc = form.desc.data
    book.account_id = current_user.id

    db.session().commit()

    return redirect(url_for("books_index"))

@app.route("/books/new/")
@login_required(role="ADMIN")
def books_form():
    return render_template("books/new.html", form = BookForm(), num=0)

@app.route("/books/delete/<book_id>/", methods=["GET"])
@login_required(role="ADMIN")
def books_delete(book_id):

    book = Book.query.get(book_id)
    db.session().delete(book)
    db.session().commit()

    return redirect(url_for("books_index"))

@app.route("/books/loan/<book_id>/", methods=["GET"])
@login_required
def books_loan(book_id):

    book = Book.query.get(book_id)

    if book.count > 0:
        book.count = book.count - 1
        loan = Loan(book.name)
        dt = datetime.datetime.now()
        dd = dt + datetime.timedelta(days=14)
        loan.due_date = dd.strftime('%d.%m.%Y')
        loan.account_id = current_user.id
        db.session().add(loan)
        db.session().commit()

    return redirect(url_for("books_index"))

@app.route("/books/", methods=["POST"])
@login_required(role="ADMIN")
def books_create():
    form = BookForm(request.form)

    if not form.validate():
        return render_template("books/new.html", form = form, num=0)

    book = Book(form.name.data)
    author = Author(form.author.data)

    db.session().add(author)

    book.author.append(author)
    book.published = form.published.data
    book.count = form.count.data
    book.desc = form.desc.data
    book.account_id = current_user.id

    db.session().add(book)
    db.session().commit()
  
    return redirect(url_for("books_index"))