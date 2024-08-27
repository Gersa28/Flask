import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Cargar credenciales de la cuenta de servicio
cred = credentials.ApplicationDefault()

# Inicializar la app de Firebase con el ID del proyecto
firebase_admin.initialize_app(cred, {
    'projectId': 'flask-app-factory-433720'  # Reemplaza 'tu-project-id' con tu ID de proyecto de Google Cloud
})

# Crear una instancia del cliente Firestore
db = firestore.client()



def get_user(user_id):
    """
    Obtiene un documento de usuario de la colección 'users' en Firestore.

    Parámetros:
    user_id (str): El ID del usuario para recuperar el documento correspondiente.

    Retorna:
    DocumentSnapshot: El documento del usuario desde Firestore.
    """
    return db.collection('users').document(user_id).get()

def user_put(user_data):
    """
    Guarda o actualiza la información del usuario en Firestore.

    Parámetros:
    user_data (UserData): Un objeto UserData que contiene el nombre de usuario y la contraseña hasheada.
    """
    # Crear una referencia al documento del usuario en la colección 'users'
    user_ref = db.collection('users').document(user_data.username)
    
    # Guardar o actualizar el documento del usuario con la contraseña hasheada
    user_ref.set({'password': user_data.password})

def get_todos(user_id):
    """
    Obtiene todas las tareas de un usuario específico desde la colección 'todos' en Firestore.

    Parámetros:
    user_id (str): El ID del usuario para recuperar las tareas correspondientes.

    Retorna:
    List[DocumentSnapshot]: Una lista de documentos que representan las tareas del usuario.
    """
    return db.collection('users')\
        .document(user_id)\
        .collection('todos').get()

def put_todo(user_id, description):
    """
    Agrega una nueva tarea a la colección 'todos' para un usuario específico en Firestore.

    Parámetros:
    user_id (str): El ID del usuario al que se le agregará la tarea.
    description (str): La descripción de la tarea a agregar.

    """
    # Crear una referencia a la subcolección 'todos' del usuario
    todos_collection_ref = db.collection('users').document(user_id).collection('todos')
    
    # Agregar un nuevo documento a la subcolección con la descripción de la tarea
    todos_collection_ref.add({'description': description, 'done': False})


def delete_todo(user_id, todo_id):
    todo_ref = db.document('users/{}/todos/{}'.format(user_id, todo_id))
    todo_ref.delete()

def update_todo(user_id, todo_id, done):
    todo_done = not bool(done)
    todo_ref = _get_todo_ref(user_id, todo_id)
    todo_ref.update({'done': todo_done})

def _get_todo_ref(user_id, todo_id):
    return db.document('users/{}/todos/{}'.format(user_id, todo_id))