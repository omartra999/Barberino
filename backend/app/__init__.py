from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

db = SQLAlchemy()
mail = Mail()

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    CORS(app)
    jwt.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    migrate = Migrate(app, db)

    with app.app_context():
        from app import routes, models
        from app.routes import bp
        app.register_blueprint(bp)
    
    return app