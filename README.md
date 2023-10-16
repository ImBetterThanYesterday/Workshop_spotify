# Workshop_spotify

**Descripción del Proyecto**: [Aquí proporciona una breve descripción de lo que hace este proyecto y su objetivo principal].

## Requisitos

- Python 3.11.6
- Docker
- PostgreSQL (ejecutado en un contenedor de Docker)
- Apache Airflow
- pip install pydrive2 pandas logging json
- pip install sqlalchemy psycopg2
- Puede instalar las dependencias con pip install -r requeriments.txt

## Estructura del Proyecto

- **docker-compose.yml**: Archivo de configuración de Docker Compose para crear y gestionar contenedores Docker.

- **/dags**: Contiene los archivos de DAG de Apache Airflow. Los archivos `.py` que orquestan el proceso ETL se encuentran aquí.

- **/logs**: Esta carpeta almacena los registros generados por Apache Airflow. Los registros son útiles para el seguimiento y la solución de problemas.

- **/config**: Contiene archivos de configuración necesarios para la ejecución del proyecto, como configuraciones de Apache Airflow.

- **/plugins**: Esta carpeta puede contener complementos personalizados que amplían la funcionalidad de Apache Airflow.

## Ejecución del Proyecto

1. Asegúrate de que Docker esté funcionando  el contenedor de Airflow:

```bash
docker-compose up 
```

2. Asegúrate de que Docker esté funcionando y ejecuta el contenedor de PostgreSQL:
```bash
sudo docker run -d --name=postgres -p 5432:5432 -v postgres-volume:/var/lib/postgresql/data -e POSTGRES_PASSWORD=mysecretpass postgres
```
3. 
 ```bash
en el navegador tienes que entrar al localhost:8080
```
4. Te Logueas con el usuario "airflow" y la contraseña "airflow"

5. ejecuta el dag
