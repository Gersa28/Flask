from flask import render_template, session, redirect, flash, url_for, request
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash

from app.forms import LoginForm

from . import auth
from app.firestore_service import *
from app.models import UserModel, UserData


@auth.route('/login', methods=['GET', 'POST'])
def login():
    print(" ESTOY EN LOGIN")
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }

    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        print("USUARIO: ", username)
        print("PASSWORD: ", password)

        user_doc = get_user(username)
        print(user_doc)

        if user_doc.to_dict() is not None:
            password_from_db = user_doc.to_dict()['password']

            if password == password_from_db:
                user_data = UserData(username, password)
                user = UserModel(user_data)

                login_user(user)

                flash('Bienvenido de nuevo','success')
                redirect(url_for('hello'))

            else:
                flash('Credenciales Inválidas','danger')
        else:
            flash('El usario no existe','info')

        return redirect(url_for('index'))

    return render_template('login.html', **context)

@auth.route('signup', methods=['GET', 'POST'])
def signup():
    # Crear una instancia del formulario de registro (LoginForm)
    signup_form = LoginForm()
    
    # Preparar el contexto para la plantilla, que incluirá el formulario de registro
    context = {
        'signup_form': signup_form
    }

    # Verificar si el método de la solicitud es POST, lo que indica que el formulario ha sido enviado
    if request.method == 'POST':
        # Obtener los datos del formulario enviados por el usuario
        username = request.form.get('username')
        password = request.form.get('password')

        # Buscar el usuario en la base de datos usando el nombre de usuario proporcionado
        user_doc = get_user(username)
        print(user_doc)  # Imprimir el documento del usuario para depuración

        # Verificar si el usuario ya existe en la base de datos
        if user_doc.to_dict() is None:
            # Si el usuario no existe, hashear la contraseña antes de guardarla
            password_hash = generate_password_hash(password)
            
            # Crear un objeto UserData con el nombre de usuario y la contraseña hasheada
            user_data = UserData(username, password_hash)
            
            # Guardar el nuevo usuario en la base de datos
            user_put(user_data)
            
            # Crear una instancia de UserModel con los datos del usuario
            user = UserModel(user_data)
            
            # Iniciar sesión automáticamente al usuario después del registro
            login_user(user)
            
            # Mostrar un mensaje de bienvenida exitoso
            flash('¡Bienvenido!', 'success')

            # Redirigir al usuario a la página principal después del registro
            return redirect(url_for('hello'))
        else:
            # Si el usuario ya existe, mostrar un mensaje de error
            flash('¡El usuario ya existe!', 'error')

    # Renderizar la plantilla de registro, pasando el contexto que incluye el formulario
    return render_template('signup.html', **context)

@auth.route('logout')
@login_required
def logout():
    logout_user()
    flash('Regresa pronto','warning')

    return redirect(url_for('auth.login'))