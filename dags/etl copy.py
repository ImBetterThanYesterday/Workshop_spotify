import pandas as pd
import logging
import json
from transform import drop_unnamed_column,borrar_nulos_spotify,crear_columnas_categoricas_,  ms_to_min,  borrar_duplicados
from transform import no_needed_columns,Transform_winner_column,drop_null_rows
from  bd_Connection import creating_engine, disposing_engine

def read_csv():
    # Reading csv file
    df = pd.read_csv("spotify_dataset.csv")
    df2 = pd.read_csv("the_grammy_awards.csv")
    print("CSV read successfully")
    print(df2)
    print(df2.columns)
    data=df.to_json(orient='records')
    
    data2=df2.to_json(orient='records') 
    spotify_df=transform_spotify(data)
    grammy_df=grammys_transform_db(data2)
    merge(grammy_df, spotify_df)
    #return grammy_df, spotify_df

    # Return or use the transformed data as needed
def transform_spotify(data):
    # CSV's transformations
    json_data = json.loads(data)
    df = pd.json_normalize(data=json_data)
    # Drop Column unnamed
    df=ms_to_min(df)
    #borrando columna que no nos proporcionan valor
    df = drop_unnamed_column(df)
    # creando columnas categoricas
    df = crear_columnas_categoricas_(df)
    # Borrando Duplicados
    df = borrar_duplicados(df)
    # borrando nulos 
    df = borrar_nulos_spotify(df)
    
    print(df.columns)
    print("CSV has ended transformation process")
    print(df)

    return df
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

def grammys_transform_db(data2):
    # CSV's transformations
    json_data = json.loads(data2)
    df = pd.json_normalize(data=json_data)
    
    #print(df)
    # Drop Columns
    df=no_needed_columns(df)    
    #  cambiando 
    df = Transform_winner_column(df)
    # Borrando Duplicados
    df = borrar_duplicados(df)
    
    #borrando registros 
    df = drop_null_rows(df)
    print(df.columns)

    print("CSV has ended transformation process")
    print(df)

    return df
    #print(df.columns)
    #return df.to_json(orient='records')


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

def merge(grammy_df, spotify_df):
    #df=read_csv()
    print("adadadad")

    #df = spotify_df.merge(grammys_df, how='left', left_on='track_name', right_on='nominee')
    df = spotify_df.merge(grammy_df, left_on='track_name', right_on='nominee', how='inner')
    print(df)
    print(df.columns)

    # Supongamos que deseas exportar merged_df a un archivo CSV llamado 'merged_data.csv'
    df.to_csv('merged_data.csv', index=False)  
    # El argumento index=False evita que se incluyan los índices en el archivo CSV

    #df = organizing_columns(df)
    #df = fill_na_after_merge(df)
    #logging.info( f"data is ready to deploy")
    #return df.to_json(orient='records')

if __name__ == "__main__":
    read_csv()