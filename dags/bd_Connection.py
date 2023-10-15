import json
from sqlalchemy import create_engine, Column, Integer, Float, String, Boolean, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Leer config desde el JSON
# with open('/home/spider/etl/workshop_02/main/db_config.json', 'r') as json_file:
#     data = json.load(json_file)
#     usuario = data["user"]
#     password = data["passwd"]
#     server = data["server"]
#     database = data["database"]

# # Configurar la URL de la base de datos para PostgreSQL
# db_url = f'postgresql+psycopg2://{usuario}:{password}@{server}/{database}'
db_params = {
    "user": "postgres",
    "password": "mysecretpass",
    "host": "localhost",
    "port": "5435",  # El puerto mapeado del contenedor (5435)
    "database": "postgres",  # Nombre de la base de datos (por defecto)
}

db_url = f'postgresql+psycopg2://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}'


#no necesario
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
