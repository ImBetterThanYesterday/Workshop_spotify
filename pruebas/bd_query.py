import psycopg2
import pandas as pd

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
csv_file_path = "C:/Users/Juanchope/IdeaProjects/Workshop_spotify/dags/the_grammy_awards.csv"  # Reemplaza con la ruta de tu archivo CSV

# Intentar conectarse a la base de datos
try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Verificar si la tabla existe
    cursor.execute(f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = '{table_name}');")
    table_exists = cursor.fetchone()[0]

    # Si la tabla no existe, créala
    if not table_exists:
        create_table_query = f"""
        CREATE TABLE {table_name} (
            year INTEGER,
            title VARCHAR,
            published_at VARCHAR,
            updated_at VARCHAR,
            nominee VARCHAR,
            artist VARCHAR,
            workers VARCHAR,
            img VARCHAR,
            winner VARCHAR
        );
        """
        cursor.execute(create_table_query)
        connection.commit()
        print(f"Tabla '{table_name}' creada.")

    # Cargar datos desde el archivo CSV
    df = pd.read_csv(csv_file_path)
    print(df)
    df.to_sql(table_name, connection, if_exists='replace', index=False)
    print(f'Datos cargados en la tabla {table_name}')

    # Confirmar los cambios
    connection.commit()

    # Consultar la tabla para verificar la carga
    cursor.execute(f"SELECT * FROM {table_name}")
    records = cursor.fetchall()

    # Imprimir los registros
    for record in records:
        print(record)

    # Cerrar la conexión
    cursor.close()
    connection.close()

except Exception as e:
    print("Error de conexión o carga de datos:", e)
