# Invera ToDo-List Challenge (Python/Django Jr-SSr)

## :hammer_and_wrench: Descarga y puesta a punto del proyecto (windows):

- Desde la terminal realizar un clone del proyecto( ejecutar un git clone https://github.com/rodri-valladares/todo-challenge-rodri.git )
- Crear entorno `python -m venv env`
- Dentro de la carpeta del entorno creado, activar entorno( `.\env\Scripts>activate`)
- Ya con el entorno activo dirigirse a la carpeta descargada/clonada, acceder a la carpeta todo_drf e instalara los paquetes: `pip install -r requirements.txt`
- Realizar y ejecutar migraciones(base de datos) : `python manage.py makemigrations` posteriormente ejecutar `python manage.py migrate`
- Crear superuser : `python manage.py createsuperuser` (se le solicitara elegir un user y un pass)

## :rocket: Ejecutar aplicación:
- Desde la terminal acceder al proyecto descargado, dentro de la carpeta "todo_drf"( \todo-challenge-rodri\todo_drf> ) ejecutar `python manage.py runserver`
- Ingresar desde cualquier navegador a la ruta local sugerida. Por lo general: http://127.0.0.1:8000/

## Como usar:
- El proyecto consiste en una aplicación web sencilla que permita a los usuarios crear y mantener una lista de tareas.
La web permite:
- Crear una tarea: Ingresar el nombre de la tarea y dar click a "Submit"
- Eliminar una tarea: Dar click al simbolo "X" correspondiente a la tarea que se quiere borrar
- Editar una tarea: Dar click al botón "Edit" correspondiente a la tarea a editar. El nombre de la tarea se ubicará nuevamente en la sección de crear nueva tarea. Colocar el nuevo nombre de la tarea y dar click al botón "Submit".
- Marcar tareas como completadas: Dar click sobre el nombre de la tarea, se le aplicará una linea por encima del nombre
- Poder ver una lista de todas las tareas existentes
- Buscar tareas por el contenido de la misma: Utilizar el cuadro con la leyenda "Buscar tarea" dar click al botón "Search"


