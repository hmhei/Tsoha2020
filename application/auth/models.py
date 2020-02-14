from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    loans = db.relationship("Loan", backref='account', lazy=True)

    def __init__(self, name, username, password, admin):
        self.name = name
        self.username = username
        self.password = password
        self.admin = admin

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        if self.admin == False:
            return ["USER"]
        else:
            return ["ADMIN"]

    @staticmethod
    def find_users_with_no_loans(returned=False):
        stmt = text("SELECT Account.id, Account.name FROM account"
                    " LEFT JOIN loan ON Loan.account_id = Account.id"
                    " WHERE (Loan.returned IS null OR Loan.returned = :returned)"
                    " GROUP BY Account.id"
                    " HAVING COUNT(Loan.id) > 0").params(returned=returned)
        res = db.engine.execute(stmt)
  
        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1]})

        return response