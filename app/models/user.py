from app.models import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)  # Cambiamos 'password' a 'password_hash'

    def set_password(self, password):
        """Encripta la contraseña antes de guardarla"""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Verifica si la contraseña ingresada es correcta"""
        return check_password_hash(self.password_hash, password)
