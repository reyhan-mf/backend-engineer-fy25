from flask import Blueprint, request, jsonify

items_bp = Blueprint('items', __name__)

@items_bp.route('/items/test', methods=['GET'])
def items_test():
    return jsonify({"message": "Items test successful"}), 200