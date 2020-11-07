from flask import jsonify
from flask_restful import Resource
from models import Post
from sqlalch import db

class JobMem(Resource):
    def get(self, job_id):
        post = db.session.query(Post).filter(Post.id == job_id).first()
        return jsonify(post)

class JobList(Resource):
    def get(self):
        posts = db.session.query(Post).all()
        return jsonify(posts)
