import pandas as pd
from sqlalchemy import create_engine

# Parámetros de conexión
db_params = {
    "host": "localhost",
    "port": "5432",
    "database": "postgres",
    "user": "postgres",
    "password": "mysecretpass",
}

# Nombre de la tabla en la base de datos
table_name = "grammys"

# Ruta al archivo CSV que deseas cargar
csv_file_path = 'the_grammy_awards.csv'  # Reemplaza con la ruta de tu archivo CSV

# Crear una conexión a la base de datos PostgreSQL
engine = create_engine(f"postgresql+psycopg2://{db_params['user']}:{db_params['password']}@{db_params['host']}:{db_params['port']}/{db_params['database']}")

# Cargar datos desde el archivo CSV a la tabla
try:
    df = pd.read_csv(csv_file_path)
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f'Datos cargados en la tabla {table_name}')
except Exception as e:
    print("Error al cargar datos:", e)
