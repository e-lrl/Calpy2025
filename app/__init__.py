from flask import Flask

def create_app():
    """
    Función factory para crear la aplicación Flask.
    Esto permite tener múltiples instancias de la app si es necesario.
    """
    app = Flask(__name__)

    # Cargar configuración
    app.config.from_object('app.config.Config')

    # Registrar blueprints (rutas modulares)
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    return app