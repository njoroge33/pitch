from . import db
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
    '''User model'''

    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    # def __repr__(self):
    #     return f'User {self.username}'

    # @property
    # def password(self):
    #     raise AttributeError('You cannot read the password attribute')

    # @password.setter
    # def password(self, password):
    #     self.pass_secure = generate_password_hash(password)


    # def verify_password(self,password):
    #     return check_password_hash(self.pass_secure,password)
