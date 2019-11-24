from . import db
from . import login
from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    '''User model'''

    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    def verify_password(self,password):
        return check_password_hash(self.password,password)

@login.user_loader
def load_user(id):
   return User.query.get(int(id))