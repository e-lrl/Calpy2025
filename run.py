from app import create_app, db
from app.models.user import User

if __name__ == '__main__':
    # Crear la aplicación
    app = create_app()

    with app.app_context():
        db.create_all()  # Asegurar que las tablas existen

        # Crear usuario admin si no existe
        if not User.query.filter_by(username="admin").first():
            new_user = User(username="admin")
            new_user.set_password("admin123")
            db.session.add(new_user)
            db.session.commit()
            print("✅ Usuario 'admin' creado. Usuario: admin | Contraseña: admin123")
        else:
            print("ℹ️ El usuario 'admin' ya existe.")

    # Ejecutar la aplicación
    app.run(host='0.0.0.0', port=5000)

