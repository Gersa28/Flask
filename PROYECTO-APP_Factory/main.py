import unittest
from flask import request, make_response, redirect, render_template, session, url_for, flash
from flask_login import login_required, current_user


from app import create_app
from app.forms import *
from app.firestore_service import *

app = create_app()


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html', error=error)


@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip

    return response


@app.route('/hello', methods=['GET', 'POST'])
@login_required
def hello():
    user_ip = session.get('user_ip')
    username = current_user.id
    todo_form = TodoForm()
    todos = get_todos(user_id=username)
    delete_form = DeleteTodoForm()    
    update_form = UpdateTodoForm()

    # Crear una lista de diccionarios de tareas
    todos_list = [doc.to_dict() for doc in todos]
    print("todos_list: ", todos_list)

    context = {
        'user_ip': user_ip,
        'username': username,
        'todos': todos,
        'todo_form' : todo_form,
        'delete_form': delete_form,        
        'update_form': update_form
    }
    print(context)

    if request.method == 'POST':
        description = request.form.get('description')
        if description:  # Validación simple
            put_todo(user_id=username, description=description)
            flash('¡Tu tarea se creó con éxito!','success')
            return redirect(url_for('hello'))
        else:
            flash('Por favor, ingresa una descripción.','danger')
    
    return render_template('hello.html', **context)
        # El operador ** se utiliza para desempaquetar un diccionario 
        # cuando se pasa como argumento a una función.
    

@app.route('/todos/delete/<todo_id>', methods=['POST'])
def delete(todo_id):
    user_id = current_user.id
    delete_todo(user_id=user_id, todo_id=todo_id)

    return redirect(url_for('hello'))

@app.route('/todos/update/<todo_id>/<int:done>', methods=['POST'])
def update(todo_id, done):
    user_id = current_user.id
    print('DONE',done)
    update_todo(user_id=user_id, todo_id=todo_id, done=done)

    return redirect(url_for('hello'))


if __name__ == "__main__":
    app.run(port=8080, debug=True)
