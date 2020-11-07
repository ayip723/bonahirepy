'''server/app.py - main api app declaration'''
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from sqlalch import db
from models import User
from users import users
from posts import posts

'''Main wrapper for app creation'''
app = Flask(__name__, static_folder='../build')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2:///test1'
CORS(app)
db.init_app(app)
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(posts, url_prefix='/posts')
##
# API routes
##

@app.route('/api/items')
def items():
  '''Sample API route for data'''
  return jsonify([{'title': 'A'}, {'title': 'B'}])

##
# View route
##

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
  '''Return index.html for all non-api routes'''
  #pylint: disable=unused-argument
  return send_from_directory(app.static_folder, 'index.html')
