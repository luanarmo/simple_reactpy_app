# Proyecto Simple ReactPy App

Este proyecto es una aplicación sencilla desarrollada con ReactPy, diseñada para probar la navegación y la creación de componentes sin estado. Incluye instrucciones para desplegar la aplicación tanto con Docker como de forma local.

# Estructura del Proyecto

- `main.py`: Archivo principal de la aplicación.
- `requirements.txt`: Requisitos de Python para la aplicación.
- `Dockerfile`: Archivo de configuración para construir la imagen Docker.
- `docker-compose.yml`: Archivo para gestionar servicios de Docker.

# Despliegue con Docker

Para desplegar la aplicación utilizando Docker, asegúrate de tener Docker instalado y ejecutando en tu máquina.

## Ejecutar la aplicación

Puedes ejecutar la aplicación usando Docker Compose. Ejecuta:

```
docker-compose up
```

Esto levantará los servicios definidos en el archivo `docker-compose.yml`. La aplicación estará disponible en `http://localhost:8000`.

# Despliegue Local

Si prefieres ejecutar la aplicación de forma local, asegúrate de tener Python instalado y sigue estos pasos:

# 1. Crear un entorno virtual

Crea un entorno virtual en la raíz del proyecto:

```
python -m venv venv
```

# 2. Activar el entorno virtual

- En Windows:

```
venv\Scripts\activate
```

- En macOS y Linux:

```
source venv/bin/activate
```

# 3. Instalar los requisitos

Instala las dependencias necesarias utilizando el archivo `requirements.txt`:

```
pip install -r requirements.txt
```

# 4. Ejecutar la aplicación

Finalmente, ejecuta la aplicación con el comando:

```
uvicorn main:app
```

La aplicación estará disponible en `http://localhost:8000`.
