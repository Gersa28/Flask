from flask import Flask, request, make_response, redirect, session, url_for, flash
from flask import render_template

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField 
from wtforms.validators import DataRequired

import unittest


app = Flask(__name__)
app.config['SECRET_KEY'] = 'SUPER SECRETO'  # ! mala práctica

tareas = ['Comprar Café', 'Estudiar Flask', 'Estudiar Inglés']

class LoginForm(FlaskForm):
    username=StringField('Username: ',validators=[DataRequired()])
    password=PasswordField('Password: ',validators=[DataRequired()])
    submit = SubmitField('Enviar')

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def Internal_Server_Error(error):
    return render_template("500.html", error=error)

@app.route('/') # En esta Ruta inicial se obtiene la IP del cliente
def index():
    User_IP = request.remote_addr
    # IP = request.remote_addr usa la función request.remote_addr para obtener la dirección IP 
    # del cliente que hizo la solicitud HTTP al servidor Flask.

    response = make_response(redirect('/hello')) # Redirect to /hello
    session['user_ip'] = User_IP

    return response

@app.route('/hello', methods=['GET', 'POST'])  # Acepta GET y POST 
def hello():
    User_IP = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    context = {
        'user_ip': User_IP,
        'tareas': tareas,
        'login_form': login_form,
        'username' : username
    }
    
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash('¡Nombre de usuario registrado con éxito!',category='success')
        return redirect(url_for('index'))    


    return render_template('hello.html', **context)
        # El operador ** se utiliza para desempaquetar un diccionario 
        # cuando se pasa como argumento a una función.


if __name__ == "__main__":
    app.run(port=8080, debug=True)
