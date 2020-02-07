from application import db
from application.models import Base

class Loan(Base):

    name = db.Column(db.String(144), nullable=False)
    returned = db.Column(db.Boolean, nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name):
        self.name = name
        self.returned = False
