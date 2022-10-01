# MISW4201-202214-Grupo07
Arquitecturas ágiles de software
> **_NOTA:_**  <br />
clonar el proyecto ejecutar el comando `git clone https://github.com/jeysonvr/MISW4201-202214-Grupo07.git` <br />
Moverse a la rama `git checkout ExperimentoSeguridad`

## Alistamiento UsuarioCliente (Front-end)

Proyecto generado con [Angular CLI](https://github.com/angular/angular-cli) versión 14.2.2.
Moverse a la carpeta `UsuarioCliente`.

### Instalar dependencias

Comando `npm i` para instalar las dependencias requeridas por el proyecto.

### Iniciar servidor de desarrollo

Comando `ng serve` para levantar el servidor. Navegar a `http://localhost:4200/`.

### Build

Comando `ng build` para construir (build) el proyecto. El build del proyecto queda en el directorio `dist/`.


## Alistamiento de microservicios (Back-end)

- Subir el virtual environment de python e instalar los requirements.

### Subir microservicios
Moverse a la carpeta `Microservicios` con el comando `cd Microservicios` <br>
Iniciar con `flask run`
 > **_NOTA:_** Validar que el front-end apunte a la url local en la que corren los microservicio (ej: localhost:5000).
