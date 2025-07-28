from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from app.database import init_db, close_db
from app.routes.auth import auth_bp
from app.routes.items import items_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize JWT
    JWTManager(app)
    
    # Initialize database
    with app.app_context():
        init_db()
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(items_bp)
    
    # Register database close function
    app.teardown_appcontext(close_db)
    
    return app