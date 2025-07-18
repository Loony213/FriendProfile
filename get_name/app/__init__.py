from flask import Flask
from flask_cors import CORS
from app.routes.name_routes import name_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(name_bp)
    return app
