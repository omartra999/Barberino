from flask import Blueprint, request, jsonify
from . import db

bp = Blueprint('main', __name__)

@bp.route('/api/registerUser', methods=['GET','POST'])
def create_user():
    return jsonify({'message': 'hello'})
