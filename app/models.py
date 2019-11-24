from . import db
from werkzeug.security import check_password_hash


class User(db.Model):
    '''User model'''

    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    def verify_password(self,password):
        return check_password_hash(self.password,password)