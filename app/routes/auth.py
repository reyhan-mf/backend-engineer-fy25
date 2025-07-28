from flask import Blueprint, request, jsonify
from app.models.user import User
from app.utils.validators import validate_email_format, validate_password
import bcrypt
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Missing required fields'}), 400
    
    email = data['email']
    password = data['password']
    
    # Validate input
    email_valid, email_error = validate_email_format(email)
    if not email_valid:
        return jsonify({'message': email_error}), 400
    
    password_valid, password_error = validate_password(password)
    if not password_valid:
        return jsonify({'message': password_error}), 400
    
    # Create user
    user_id = User.create(email, password)
    if not user_id:
        return jsonify({'message': 'Email already exists'}), 400
    
    return jsonify({'message': 'User registered successfully'}), 201

@auth_bp.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'message': 'Missing required fields'}), 400
    
    user = User.get_by_email(data['email'])
    if not user:
        return jsonify({'message': 'Invalid email or password'}), 401
    
    if not bcrypt.checkpw(data['password'].encode('utf-8'), user['password']):
        return jsonify({'message': 'Invalid email or password'}), 401
    
    access_token = create_access_token(identity=str(user['id']))
    return jsonify({'token': access_token}), 200

@auth_bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.get_by_id(user_id)
    return jsonify({'email': user['email'], 'id': user_id}), 200

