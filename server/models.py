from sqlalch import db
from dataclasses import dataclass

@dataclass
class User(db.Model):
    __tablename__ = 'users'
    id: int = db.Column(db.BigInteger, primary_key=True)
    username: str = db.Column(db.String, unique=True, nullable=False)
    email: str = db.Column(db.String, unique=True, nullable=False)
    posts = db.relationship('Post', back_populates='user')

@dataclass
class Post(db.Model):
    __tablename__ = 'posts'
    id: int = db.Column(db.BigInteger, primary_key=True)
    title: str = db.Column(db.String)
    content: str = db.Column(db.String)
    user_id: int = db.Column(db.BigInteger, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='posts')
