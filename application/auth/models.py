from application import db
from application.models import Base

from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    address = db.Column(db.String(144), nullable=False)
    phone = db.Column(db.String(144), nullable=False)
    admin = db.Column(db.Boolean, nullable=False)

    loans = db.relationship("Loan", backref='account', lazy=True)

    def __init__(self, name, username, password, address, phone, admin):
        self.name = name
        self.username = username
        self.password = password
        self.address = address
        self.phone = phone
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

    def is_admin(self):
        return self.admin

    @staticmethod
    def list_users_with_loans(returned=False):
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

    @staticmethod
    def list_users_with_loans_and_loans_amount(returned=False):
        stmt = text("SELECT Account.id, Account.name, COUNT(*) FROM account"
                    " INNER JOIN loan ON Loan.account_id = Account.id"
                    " WHERE (Loan.returned IS null OR Loan.returned = :returned)"
                    " GROUP BY Account.id"
                    " HAVING COUNT(Loan.id) > 0"
                    " ORDER BY Account.name").params(returned=returned)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "loans":row[2]})

        return response