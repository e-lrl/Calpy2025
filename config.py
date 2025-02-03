import os

class Config:
    """
    Clase de configuración de la aplicación.
    Aquí puedes agregar variables como secret_key, database_uri, etc.
    """
    DEBUG = True
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecreto')    # Cambia esto por algo seguro en producción

    # Configurar PostgreSQL con psycopg2
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://postgres:chuschus@localhost/postgres'
    )
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
