from application import db
from application.models import Base

class Book(Base):

    name = db.Column(db.String(144), nullable=False)
    published = db.Column(db.Integer, nullable=False)
    # author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.published = False
