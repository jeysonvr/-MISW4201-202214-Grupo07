# -MISW4201-202214-Grupo07
Arquitecturas ágiles de software

## Alistamiento

- Subir el virtual environment de python e instalar los requirements.
- Crear variable de entorno:

export AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=experiment092022;AccountKey=bXSjb/KxRpXyKu0d9xW9KMqP0YrZpJvcgiQXMUDq9PIkbJJ/y1lg2N5F9qAAkEaeLl39Ri+BQ0WK+AStTp1apw==;EndpointSuffix=core.windows.net"

Nota: Por cada microservicio a ejecutar se debe realizar el alistamiento en terminales diferentes.

### Crear la cola
 Solo es necesario una vez, ya está creada actualemente. <br>
 Iniciar con `flask run` , dentro de la carpeta flaskr. <br>
 > **_NOTA:_** Este paso únicamente se debe realizar si se desea utilizar una cola de mensajes nueva. En caso de crear una cola nueva, es necesario cambiar en el archivo `app.py` de cada microservicio el nombre de la cola creada `q_name`.

### Subir microservicio 1
Microservicio encargado de enviar mensajes a una cola en azure <br>
Iniciar con `flask run` , dentro de la carpeta `microservicio_1`

### Subir microservicio 2
Microservicio encargado de procesar los mensajes de la cola en azure <br>
Iniciar con `flask run` , dentro de la carpeta `microservicio_2`
