from flask import Blueprint
from models import User
from sqlalch import db

users = Blueprint('users', __name__)

@users.route('/')
def hello_user():
  # return 'hello'
  user = db.session.query(User).first()
  return user.username if user else 'No name'
