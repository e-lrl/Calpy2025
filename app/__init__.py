from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
from app.models import db
from app.models.user import User

login_manager = LoginManager()

def create_app():
    """
    Función factory para crear la aplicación Flask.
    Esto permite tener múltiples instancias de la app si es necesario.
    """
    app = Flask(__name__)

    # Cargar configuración
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Registrar blueprints (rutas modulares)
    from app.routes.main import main_bp
    from app.routes.auth import auth_bp
    from app.routes.dashboard import dashboard_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    return app