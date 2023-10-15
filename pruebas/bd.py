import pandas as pd
from sqlalchemy import create_engine
from  bd_Connection import creating_engine, disposing_engine
# Ruta al archivo CSV
csv_file = 'the_grammy_awards.csv'

# Carga el archivo CSV en un DataFrame
#df = pd.read_csv(csv_file)
# Configura la conexión a la base de datos PostgreSQL utilizando SQLAlchemy
# db_params = {
#     "user": "postgres",
#     "password": "mysecretpass",
#     "host": "localhost",
#     "port": "5435",  # El puerto mapeado del contenedor (5435)
#     "database": "postgres",  # Nombre de la base de datos (por defecto)
# }
def read_db():
    # Hacer la consulta SQL a Grammys
    consulta_sql = "SELECT * FROM merge"
    # Crear el engine para conectarse a la base de datos
    engine = creating_engine()
    grammys_df = pd.read_sql(consulta_sql, con=engine)
    #Cerramos la conexion a la db
    disposing_engine(engine)
    print(grammys_df)
    print(grammys_df.columns)
read_db()

def load(**kwargs):
    # logging.info("starting load proc")
    # ti = kwargs["ti"]
    # str_data = ti.xcom_pull(task_ids="merge")
    # json_data = json.loads(str_data)
    #df = pd.json_normalize(data=json_data)
    engine = creating_engine()

    df=pd.read_csv("merged_data.csv")
    print(df)
    df.to_sql('merge', engine, if_exists='replace', index=False)

    #Cerramos la conexion a la db
    disposing_engine(engine)
    #df.to_csv("data_result.csv", index=False)

#read_db()
#load()
# engine = create_engine(f'postgresql+psycopg2://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}')

# # Carga el DataFrame en la base de datos
# table_name = 'grammys'
# df.to_sql(table_name, con=engine, if_exists='replace', index=False)

# # Cierra la conexión
# engine.dispose()

