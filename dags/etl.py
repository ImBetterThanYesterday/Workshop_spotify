import pandas as pd
import logging
import json
from transform import drop_unnamed_column,borrar_nulos_spotify,crear_columnas_categoricas_,  ms_to_min,  borrar_duplicados
from transform import no_needed_columns,Transform_winner_column,drop_null_rows
from  bd_Connection import creating_engine, disposing_engine
from load_To_Drive import subir_archivo

def read_csv():
    # Reading csv file
    spotify_df = pd.read_csv("/opt/airflow/dags/spotify_dataset.csv")
    logging.info("csv read succesfully")
    return spotify_df.to_json(orient='records')
    #return grammys_df, spotify_df

    # Return or use the transformed data as needed
def transform_spotify(**kwargs):
    ti = kwargs["ti"]
    str_data = ti.xcom_pull(task_ids="read_csv")
    json_data = json.loads(str_data)
    spotify_df = pd.json_normalize(data=json_data)
    
    # Spotify transformations
    spotify_df = pd.json_normalize(data=json_data)
    # Drop Column unnamed
    spotify_df=ms_to_min(spotify_df)
    #borrando columna que no nos proporcionan valor
    spotify_df = drop_unnamed_column(spotify_df)
    # creando columnas categoricas
    spotify_df = crear_columnas_categoricas_(spotify_df)
    # Borrando Duplicados
    spotify_df = borrar_duplicados(spotify_df)
    # borrando nulos 
    spotify_df = borrar_nulos_spotify(spotify_df)
    
    print(spotify_df.columns)
    print("CSV has ended transformation process")
    print(spotify_df)
    logging.info("csv has ended transformation proccess")
    return spotify_df.to_json(orient='records')
    #print(df.columns)
    #return df.to_json(orient='records')

#
def read_db():
    # Hacer la consulta SQL a Grammys
    query = "SELECT * FROM grammys"
    # Crear el engine para conectarse a la base de datos
    engine = creating_engine()
    grammys_df = pd.read_sql(query, con=engine)
    #Cerramos la conexion a la db
    disposing_engine(engine)
    print(grammys_df)

    logging.info("database read succesfully")
    return grammys_df.to_json(orient='records')

def grammys_transform_db(**kwargs):
    ti = kwargs["ti"]
    str_data = ti.xcom_pull(task_ids="read_db")
    json_data = json.loads(str_data)
    grammys_df = pd.json_normalize(data=json_data)
    logging.info(f"data from db has started transformation proccess")
    # transformations
    # Drop Columns
    grammys_df=no_needed_columns(grammys_df)    
    #  cambiando 
    grammys_df = Transform_winner_column(grammys_df)
    # Borrando Duplicados
    grammys_df = borrar_duplicados(grammys_df)
    #borrando registros 
    grammys_df = drop_null_rows(grammys_df)
    print(grammys_df.columns)

    print("CSV has ended transformation process")
    print(grammys_df)

    #function transformed
    return grammys_df.to_json(orient='records')
    #print(df.columns)
    #return df.to_json(orient='records')

def merge(**kwargs):
    ti = kwargs["ti"]
    logging.info( f"in the merge function")
    str_data = ti.xcom_pull(task_ids="transform_csv")
    json_data = json.loads(str_data)
    spotify_df = pd.json_normalize(data=json_data)
    #df=read_csv()
    print("adadadad")

    logging.info( f"grammys is entering to the merge function")
    str_data = ti.xcom_pull(task_ids="transform_db")
    json_data = json.loads(str_data)
    grammys_df = pd.json_normalize(data=json_data)

    #df = spotify_df.merge(grammys_df, how='left', left_on='track_name', right_on='nominee')
    df = spotify_df.merge(grammys_df, left_on='track_name', right_on='nominee', how='inner')
    print(df)
    print(df.columns)
    logging.info( f"data is ready to deploy")
    return df.to_json(orient='records')

def load(**kwargs):
    logging.info("starting load proc")
    ti = kwargs["ti"]
    str_data = ti.xcom_pull(task_ids="merge")
    json_data = json.loads(str_data)
    df = pd.json_normalize(data=json_data)
    engine = creating_engine()

    df.to_sql('merge', engine, if_exists='replace', index=False)

    #Cerramos la conexion a la db
    disposing_engine(engine)
    df.to_csv("data_result.csv", index=False)
    logging.info( f"data is ready to deploy")
    return df.to_json(orient='records')

def store(**kwargs):
    logging.info("starting store process")
    ti = kwargs["ti"]
    str_data = ti.xcom_pull(task_ids="load")
    json_data = json.loads(str_data)
    df = pd.json_normalize(data=json_data)
    
    ruta="/opt/airflow/dags/merged_data.csv"
    subir_archivo(ruta,"1WZbU6FwuU5SIMST5uDKXMY-VFXWPNS9n")  
    logging.info( f"data has completed the process")