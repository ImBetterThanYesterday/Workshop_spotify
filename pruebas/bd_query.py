import psycopg2
# Parámetros de conexión
db_params = {
    "host": "localhost",          # La dirección IP o el nombre de host del contenedor
    "port": "5435",               # El puerto mapeado del contenedor (5435)
    "database": "postgres",       # Nombre de la base de datos (por defecto)
    "user": "postgres",           # Usuario de la base de datos
    "password": "mysecretpass",   # Contraseña del usuario
}

# Intentar conectarse a la base de datos
try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Ejecutar consultas aquí
    cursor.execute("SELECT version();")
    version = cursor.fetchone()
    print("Conexión exitosa a PostgreSQL:", version)

    create_table_query = """
    CREATE TABLE IF NOT EXISTS grammys (
    year INTEGER,
    title varchar,
    published_at varchar,
    updated_at varchar,
    nominee varchar,
    artist varchar,
    workers varchar,
    img varchar,
    winner varchar 
    );
    """
    cursor.execute(create_table_query)
    connection.commit()
    
    #creando tabla merge 
    create_table_query = """
    CREATE TABLE IF NOT EXISTS merged (
    track_id varchar,
    artists varchar,
    album_name varchar,
    track_name varchar,
    popularity INTEGER,
    duration_ms INTEGER,
    explicit BOOLEAN,
    danceability FLOAT,
    energy FLOAT,
    key INTEGER,
    loudness FLOAT,
    mode INTEGER,
    speechiness FLOAT,
    acousticness FLOAT,
    instrumentalness varchar,
    liveness FLOAT,
    valence FLOAT,
    tempo FLOAT,
    time_signature INTEGER,
    track_genre varchar,
    duration_min FLOAT,
    danceability_category varchar,
    energy_category varchar,
    valence_category varchar,
    popularity_category varchar,
    duration_categorys varchar,
    year INTEGER,
    category varchar,
    nominee varchar,
    artist varchar,
    winner INTEGER 
    );
    """
    cursor.execute(create_table_query)
    connection.commit()

    # Consultar el catálogo information_schema para obtener las tablas
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public'")
    tables = cursor.fetchall()

    # Imprimir las tablas
    print("Tablas en la base de datos:")
    for table in tables:
        print(table[0])
        
    #table_to_delete = "awards"
    #cursor.execute("DROP TABLE Applicants_def")

    # Intenta conectarte a la base de datos
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Realiza la consulta SELECT
    cursor.execute("SELECT * FROM grammys")

    # Recupera todos los registros
    records = cursor.fetchall()

    # Imprime los registros
    for record in records:
        print(record)




 


    # Confirmar los cambios
    connection.commit()

    # Cerrar la conexión
    cursor.close()
    connection.close()

except Exception as e:
    print("Error de conexión:", e)