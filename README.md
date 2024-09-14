# Flask
Prácticas Con Flask

[Teoría y Contexto ](https://www.notion.so/german-salina/Flask-9b623d6a80d94c699381bd1de9dca290)


# **INVERA: ToDo-List Challenge**

## 👁 Información

**Contacto:** Germán Salina  
**Email:** gersalina28@gmail.com  
**Tel:** +54 9 0343 154 599358  
**Cel:** +54 9 3434599358  
**LinkedIn:** [Bioingeniero Germán Salina](https://www.linkedin.com/in/ingeniero-salina-german/)  
**Página Web:** [Blog Personal](https://www.notion.so/775f8b5f910841a19ea81c4dbac66aec?pvs=21)  

---

## 🗝️ Requisitos

<details>
  <summary>Conocimientos previos</summary>
  
  - Terminal y Línea de Comandos
  - [Python 3](https://www.python.org/)
  - Django
  - Bases de Datos
  - Docker
  - Testing
  - Django Rest Framework (DRF)

</details>

<details>
  <summary>Herramientas necesarias</summary>
  
  - Computadora con sistema operativo Windows, MacOS o Linux.
  - [Visual Studio Code](https://code.visualstudio.com/)
  - Docker
  - Postman o Thunder Client

</details>

---

## 🎯 Objetivos

<details>
  <summary>Objetivos del proyecto</summary>
  
  - Autenticarse
  - Crear una tarea
  - Eliminar una tarea
  - Marcar tareas como completadas
  - Poder ver una lista de todas las tareas existentes
  - Filtrar/buscar tareas por fecha de creación y/o por el contenido de la misma

</details>

---

## 📜 Resumen

<details>
  <summary>Descripción del Challenge</summary>
  
  **Qué queremos que hagas:**

  - El Challenge consiste en crear una aplicación web sencilla que permita a los usuarios crear y mantener una lista de tareas.
  - La entrega del resultado será en un nuevo fork de este repo y deberás hacer una pequeña demo del funcionamiento y desarrollo del proyecto ante un comité técnico.
  - Podes contactarnos en caso que tengas alguna consulta.

  **Qué evaluamos:**

  - Desarrollo utilizando Python, Django. No es necesario crear un Front-End, pero sí es necesario tener una API que permita cumplir con los objetivos de arriba.
  - Uso de librerías y paquetes estándar que reduzcan la cantidad de código propio añadido.
  - Calidad y arquitectura de código.
  - [Bonus] Manejo de logs.
  - [Bonus] Creación de tests (unitarias y de integración)
  - [Bonus] Unificar la solución propuesta en una imagen de Docker para que pueda ser ejecutada en cualquier ambiente.
  
</details>

---

# Guía de Instalación

<details>
  <summary>Clonar la Aplicación y ubicarse en el directorio del proyecto</summary>

  ```bash
  git clone https://github.com/<usuario>/<repo>.git
  cd nombre_del_proyecto
  ```

</details>

<details>
  <summary>Instalación mediante Entorno Virtual</summary>

  ### Windows

  ```bash
  python --version
  pip install virtualenv
  python -m venv venv
  .\venv\Scripts\Activate
  pip list
  python.exe -m pip install --upgrade pip
  pip install -r requirements.txt
  python manage.py createsuperuser
  python manage.py makemigrations
  python manage.py migrate
  python manage.py runserver
  ```

  ### Linux

  ```bash
  python3 --version
  pip3 install virtualenv
  python3 -m venv venv
  source venv/bin/activate
  pip list
  python3 -m pip install --upgrade pip
  pip install -r requirements.txt
  python3 manage.py createsuperuser
  python3 manage.py makemigrations
  python3 manage.py migrate
  python3 manage.py runserver
  ```

</details>

<details>
  <summary>Instalación utilizando Docker</summary>

  ```bash
  # Verificar la versión de Docker instalada
  docker --version

  # Crear la imagen llamada "proyectotodo" usando el Dockerfile actual
  sudo docker build -t proyectotodo .

  # Ejecutar el contenedor mapeando el puerto 8000 del contenedor al puerto 7000 del host
  docker run -d -p 7000:8000 --name proyectotodo proyectotodo

  # Listar los contenedores activos para verificar el nombre correspondiente
  docker ps

  # Acceder al contenedor en ejecución usando el nombre o ID del contenedor
  docker exec -it proyectotodo /bin/bash

  # Crear un superusuario para la aplicación de Django dentro del contenedor
  python manage.py createsuperuser

  # Salir del bash
  exit

  # Detener el contenedor en ejecución de forma ordenada
  docker stop proyectotodo
  ```

</details>

---

# Aplicación WEB

<details>
  <summary>Versión Gráfica</summary>
  
  ![image](url-de-imagen)

</details>

---

# Peticiones a la API

<details>
  <summary>Documentación de la API</summary>
  
  http://127.0.0.1:8000/api/docs/

</details>

<details>
  <summary>CRUD de Tareas</summary>

  **POST: Crear Tarea**

  ```json
  {
      "name": "Nueva tarea",
      "description": "Descripción de la nueva tarea",
      "status": "not_started"
  }
  ```

  **GET: Listar Tareas**

  http://127.0.0.1:8000/api/tasks/

</details>

---

# Testing

<details>
  <summary>Ejecutar Tests</summary>

  Para correr los tests ejecuta:

  ```bash
  python manage.py test
  ```

</details>

---

# Manejo de Logs

<details>
  <summary>Logs de la Aplicación</summary>

  Ejemplo de un log en el archivo:

  ```
  INFO 2024-09-13 15:45:30 views Tarea creada por testuser
  INFO 2024-09-13 15:46:12 api Listando tareas para el usuario: testuser
  ```

</details>
