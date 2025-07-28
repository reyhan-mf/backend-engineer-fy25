from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/auth/test', methods=['GET'])
def auth_test():
    return jsonify({"message": "Auth test successful"}), 200