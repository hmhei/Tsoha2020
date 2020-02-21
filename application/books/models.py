from application import db
from application.models import Base
from application.authors.models import Author

from sqlalchemy.sql import text

bookAuthors = db.Table('book_authors',
    db.Column('book_id', db.Integer, db.ForeignKey('book.id')),
    db.Column('author_id', db.Integer, db.ForeignKey('author.id'))
)

class Book(Base):

    name = db.Column(db.String(144), nullable=False)
    author = db.relationship(
        "Author", secondary=bookAuthors, backref='book_authors', lazy=True)
    published = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    
    # author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.published = False

    @staticmethod
    def list_authors(bookid):
        stmt = text("SELECT Author.name FROM author"
                    " INNER JOIN book_authors ON book_authors.author_id = Author.id"
                    " LEFT JOIN book ON Book.id = book_authors.book_id)"
                    " WHERE Book.id = :bookid"
                    " GROUP BY Book.id").params(bookid=bookid)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"authors": row[0]})

        return response
