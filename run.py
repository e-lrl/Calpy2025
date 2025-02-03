from app import create_app

if __name__ == '__main__':
    # Crear la aplicación
    app = create_app()

    # Ejecutar la aplicación
    app.run(host='0.0.0.0', port=5000)