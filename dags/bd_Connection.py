from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

db_params = {
    "user": "postgres",
    "password": "mysecretpass",
    "host": "127.0.0.1",
    "port": "5432",  # El puerto mapeado del contenedor (5435)
    "database": "postgres",  # Nombre de la base de datos (por defecto)
}

db_url = f'postgresql+psycopg2://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}'



Base = declarative_base()

# Función para crear el motor (engine)
def creating_engine():
    engine = create_engine(db_url)
    return engine

# Función para crear las sesiones
def creating_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

# Función para cerrar la sesión
def closing_session(session):
    session.close()

# Función para cerrar el motor (engine)
def disposing_engine(engine):
    engine.dispose()
    print("Engine cerrado")
