from flask import Blueprint, render_template

# Creamos un blueprint para las rutas principales
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    """
    Ruta principal que muestra "Hola Mundo" utilizando una plantilla.
    """
    return render_template('index.html', message="pepe")