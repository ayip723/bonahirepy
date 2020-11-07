from flask import Blueprint, jsonify
from models import Post
from sqlalch import db

posts = Blueprint('posts', __name__)

@posts.route('/')
def show_posts():
    posts = db.session.query(Post).all()
    return jsonify(posts)
