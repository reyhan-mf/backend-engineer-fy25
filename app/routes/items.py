from flask import Blueprint, request, jsonify
from app.models.item import Item
from app.utils.validators import validate_item
from flask_jwt_extended import get_jwt_identity, jwt_required

items_bp = Blueprint('items', __name__)

@items_bp.route('/items/test', methods=['GET'])
def items_test():
    return jsonify({"message": "Items test successful"}), 200


@items_bp.route('/items', methods=['POST'])
@jwt_required()
def create_item():
    data = request.get_json()
    
    if not data or 'name' not in data:
        return jsonify({'message': 'Missing required fields'}), 400
    
    name = data['name']
    description = data.get('description', '')
    status = data.get('status', 'pending')
    
    valid, error = validate_item(name, description)
    if not valid:
        return jsonify({'message': error}), 400
    
    user_id = get_jwt_identity()
    item_id = Item.create(name, description, user_id, status)
    
    return jsonify({'message': 'Item created successfully', 'id': item_id}), 201


@items_bp.route('/items', methods=['GET'])
def get_items():
    page = request.args.get('page', 1, type=int)
    limit = request.args.get('limit', 10, type=int)
    
    if page < 1:
        page = 1
    if limit < 1 or limit > 100:
        limit = 10
    
    result = Item.get_all(page, limit)
    return jsonify(result), 200