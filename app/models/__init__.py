from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Importar modelos aquí para registrarlos en SQLAlchemy
from app.models.user import User