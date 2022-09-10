# -MISW4201-202214-Grupo07
Arquitecturas ágiles de software

## Alistamiento

- Subir el virtual environment de python e instalar los requirements.
- Crear variable de entorno:

export AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=https;AccountName=experiment092022;AccountKey=bXSjb/KxRpXyKu0d9xW9KMqP0YrZpJvcgiQXMUDq9PIkbJJ/y1lg2N5F9qAAkEaeLl39Ri+BQ0WK+AStTp1apw==;EndpointSuffix=core.windows.net"

Nota: Por cada microservicio a ejecutar se debe realizar el alistamiento en terminales diferentes.

### Crear la cola
 Solo es necesario una vez, ya esta creada actualemente.
 Iniciar con flask run , dentro de la carpeta flaskr

### Subir microservicio 1
Microservicio encargado de enviar mensajes a una cola en azure
Iniciar con flask run , dentro de la carpeta flaskr

### Subir microservicio 2
Microservicio encargado de procesar los mensajes de la cola en azure
Iniciar con flask run , dentro de la carpeta flaskr
