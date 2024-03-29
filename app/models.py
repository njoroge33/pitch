from . import db
from . import login
from werkzeug.security import check_password_hash
from flask_login import UserMixin
import enum
from sqlalchemy import Enum
import arrow


class User(UserMixin, db.Model):
    '''User model'''

    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(255),unique = True,index = True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    def verify_password(self,password):
        return check_password_hash(self.password,password)

# class CategoryEnum(enum.Enum):
#     product = 'product'
#     interview = 'interview'
#     promotion = 'promotion'
choices = ['product', 'interview', 'promotion']
category_enum = Enum(*choices, name='category_enum')

class Pitch(db.Model):
    
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    description = db.Column(db.String(), index = True)
    title = db.Column(db.String())
    category = db.Column(category_enum, server_default='product')
    date = db.Column(db.DateTime, nullable=False, default=arrow.utcnow().datetime)
    upvotes = db.Column(db.Integer, default=0)
    downvotes = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'Pitch {self.description}'
    

    @classmethod
    def get_pitches(cls,owner_id):
        pitches = Pitch.query.filter_by(owner_id=owner_id).all()
        return pitches

class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer,primary_key=True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)
    description = db.Column(db.Text)
    def __repr__(self):
        return f"Comment : id: {self.id} comment: {self.description}"
        
@login.user_loader
def load_user(id):
   return User.query.get(int(id))