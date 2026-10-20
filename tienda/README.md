# Proyecto Tienda - Django

Breve descripción: Aplicación web desarrollada en Django para la gestión de productos de una tienda. Permite registrar productos (nombre, precio y descuento), listarlos y calcular el precio final aplicando los descuentos correspondientes.

## Requisitos previos

- Python 3.10 o superior
- Django 4.x o superior

## Instrucciones para ejecutar el proyecto

1. **Clonar o descargar el proyecto** y acceder a la carpeta raíz:

   ```bash
   cd tienda

2. **Crear y activar un entorno virtual:**

    En Windows:
    ```bash

    python -m venv venv
    venv\Scripts\activate
    ```
    En Mac/Linux:
    ```bash

    python3 -m venv venv
    source venv/bin/activate

3.    Instalar las dependencias:
    bash

    pip install django

4.    Aplicar las migraciones para crear la base de datos:
    bash

    python manage.py migrate

5.    Ejecutar el servidor de desarrollo:
    bash

    python manage.py runserver

6.    Acceder a la aplicación en el navegador:

        Listado de productos: http://127.0.0.1:8000/productos/

        Añadir nuevo producto: http://127.0.0.1:8000/productos/nuevo/

Medida de seguridad para producción

Antes de desplegar en producción, es imprescindible establecer la variable DEBUG = False en el archivo settings.py y configurar correctamente ALLOWED_HOSTS con el dominio real del servidor. De lo contrario, Django mostrará información sensible sobre el código y la configuración en caso de error, lo que supone un grave riesgo de seguridad. También se recomienda usar una base de datos robusta (como PostgreSQL) y servir los archivos estáticos mediante un servidor web como Nginx o Apache.