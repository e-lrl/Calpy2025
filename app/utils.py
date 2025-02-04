from flask import abort
from flask_login import current_user
from functools import wraps

def role_required(role):
    """ Decorador para restringir el acceso a usuarios con cierto rol """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role != role:
                abort(403)  # Acceso prohibido
            return f(*args, **kwargs)
        return decorated_function
    return decorator
