from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token 
from app.mail_utilis.utilis import send_verification_email
from .db_helper import user_exists, email_exists, add_user

bp = Blueprint('main', __name__)

@bp.route('/api/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()

        if (user_exists(data['username'])):
            return jsonify({'message': 'Username already exists'}), 400
        if (email_exists(data['email'])):
            return jsonify({'message': 'Email already exists'}), 400

        add_user(data['first_name'], data['last_name'],data['username'],data['email'],data['password'])

        token = create_access_token(identity=data['email'])

        send_verification_email(data['email'], token)

        return jsonify({'message': 'User registered successfully. Check your email for verification.'}), 201