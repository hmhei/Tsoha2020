from application import db
from application.models import Base
from application.authors.models import Author

from sqlalchemy.sql import text

bookAuthor = db.Table('book_author',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'))
)

class Book(Base):

    name = db.Column(db.String(144), nullable=False)
    author = db.relationship(
        "Author", secondary=bookAuthor, backref='book_author', lazy=True, cascade="delete")
    published = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.String(1050), nullable=False)
    
    # author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __init__(self, name):
        self.name = name

    @staticmethod
    def list_authors(bookid):
        stmt = text("SELECT Author.name "
                    "FROM author "
                    "JOIN book_author ON book_author.author_id = Author.id "
                    "JOIN book ON Book.id = book_author.book_id "
                    "WHERE Book.id = :bookid "
                    "GROUP BY Author.name, Book.id").params(bookid=bookid)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name": row[0]})

        return response
