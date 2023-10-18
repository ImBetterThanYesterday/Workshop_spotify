# Workshop_spotify

**Descripción del Proyecto**: "Este proyecto combina un dataset de Spotify con información detallada sobre canciones, incluyendo características como tempo, energía y popularidad, con un conjunto de datos de los premios Grammy que contiene información sobre las canciones y artistas galardonados a lo largo de los años. El objetivo de este proyecto es analizar la relación entre las características musicales de las canciones, su éxito en términos de reproducciones y premios Grammy, identificando patrones y tendencias que puedan arrojar luz sobre los criterios de selección de los ganadores de estos prestigiosos premios y su relación con las preferencias del público.".

## Requisitos

- Python 3.11.6
- Docker
- PostgreSQL (ejecutado en un contenedor de Docker)
- Apache Airflow


## Estructura del Proyecto

- **docker-compose.yml**: Archivo de configuración de Docker Compose para crear y gestionar contenedores Docker de Airflow.

- **/dags**: Contiene los archivos de DAG de Apache Airflow. Los archivos `.py` que orquestan el proceso ETL se encuentran aquí.

- **/logs**: Esta carpeta almacena los registros generados por Apache Airflow. Los registros son útiles para el seguimiento y la solución de problemas.

- **/config**: Contiene archivos de configuración necesarios para la ejecución del proyecto, como configuraciones de Apache Airflow.

- **/plugins**: Esta carpeta puede contener complementos personalizados que amplían la funcionalidad de Apache Airflow.

- **/pruebas**: Esta carpeta contiene alguno de los test a las funciones que puede realizar, sin necesidad de usar airflow.

- **EDA_Grammys.ipynb**: Esta Notebook Contiene el Analisis Exploratorio de el dataset grammys_awards.csv .

- **/EDA_Spotify_Dataset.ipynb**:  Este Notebook Contiene el Analisis Exploratorio de el dataset spotify_dataset.csv .

- **/GRAFICAS.pdf**: Este PDF Contiene El Dashboard de las Graficas realizadas con PowerBi.

- **/requeriments.txt**: Este txt contiene Las Dependencias Necesesarias para correr el Proyecto.

## Ejecución del Proyecto

1. Asegúrate de que Docker esté funcionando y ejecutamos el contenedor de Airflow:

```bash
docker-compose up 
```

2. Asegúrate de que Docker esté funcionando y ejecuta el contenedor de PostgreSQL:
```bash
sudo docker run -d --name=postgres -p 5435:5432 -v postgres-volume:/var/lib/postgresql/data -e POSTGRES_PASSWORD=mysecretpass postgres
```
3. en su IDE instale las dependencias
    ```bash
 pip install -r requeriments.txt
 # tambien puede hacer 
 pip install pydrive2 
 pip install pandas
 pip install logging 
 pip install json
 pip install psycopg2
 pip install sqlalchemy
```
## Prepara la Base De Datos:
4. Debes Crear la tabla y subir los datos a la base de datos ejecutando el archivo pruebas/bd_query.py
 ```bash
python pruebas/bd_query.py
```

5.Para que el contenedor de airflow y postgres se puedan comunicar, Debes ir al fichero /dags/bd_Connection.py (linea 8). Y  reemplazar el host por tu ip
   ```bash
db_params = {
    "user": "postgres",
    "password": "mysecretpass",
    "host": "AQUI DEBES PONER TU IP ",
    "port": "5435",  # El puerto mapeado del contenedor (5435)
    "database": "postgres",  # Nombre de la base de datos (por defecto)
}
```
6.La ip la puedes ver ipconfig , ifconfig dependiendo si estas en windows , linux o mac.
 ```bash
ipconfig #windows
ifconfig #linux y mac
```
## Si quieres Configurar la subida del dataset final a Google Drive, Sigue estos Pasos, si no obvialos.
7. Configurando Google Drive Api
- Debes borrar los archivos client_secrets.json,credentials_module.json y remplazarlos por los tuyos.
- en el fichero etl.py debes remplazar en la linea 135 el id de tu carpeta de Google Drive.
- Ve a la Documentación y sigue los Pasos en la Sección Load_To_Drive.
```bash
id_folder="AQUI PONES EL ID DE TU FOLDER"
```
 ## ojo 
 **Si no Hiciste el Paso 7, para que te corra el Proyecto, debes comentar las siguientes lineas.**

 - **etl.py**:  Debes comentar la linea 7 **from load_To_Drive import subir_archivo** y la linea 136 **subir_archivo(ruta_archivo,id_folder)**

## Entramos a Airflow
8. en el navegador tienes que entrar al:
 ```bash
 localhost:1080
```
9. Te Logueas con el usuario "airflow" y la contraseña "airflow".

10. Activas el Dag dandole al slide y Le das a la flecha Para Para comenzar el Pipeline.
