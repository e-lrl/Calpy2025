from flask import Blueprint, render_template
from flask_login import login_required
from app.utils import role_required  # Importar el decorador

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
@login_required
@role_required("admin")  # Solo administradores pueden acceder
def admin_dashboard():
    return render_template('admin_dashboard.html')
