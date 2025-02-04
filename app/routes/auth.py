from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models.user import User, db
import logging  # Importar logging

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.dashboard'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash("Inicio de sesión exitoso", "success")

            log_msg = f"Usuario '{username}' inició sesión correctamente."
            print(log_msg)  # Mostrar en consola
            logging.info(log_msg)  # Guardar en log.txt

            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('dashboard.dashboard'))
        else:
            flash("Usuario o contraseña incorrectos", "danger")

            log_msg = f"Intento fallido de inicio de sesión para el usuario '{username}'."
            print(log_msg)  # Mostrar en consola
            logging.warning(log_msg)  # Guardar en log.txt

    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    username = current_user.username
    logout_user()
    flash("Sesión cerrada correctamente", "info")

    log_msg = f"Usuario '{username}' cerró sesión."
    print(log_msg)  # Mostrar en consola
    logging.info(log_msg)  # Guardar en log.txt

    return redirect(url_for('auth.login'))
