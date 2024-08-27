from flask_testing import TestCase
from flask import current_app, url_for

from main import app


class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False # Solo para Testing

        return app

    def test_app_exists(self): # La aplicación existe?
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self): # La app está en modo testing?
        self.assertTrue(current_app.config['TESTING'])

    def test_index_redirects(self): # El index redirige a hello?
        response = self.client.get(url_for('index'))
        self.assertRedirects(response, url_for('hello'))
        # subraya **assertRedirects** y con click derecho despliega las opciones, escoge la primera "Go to definition" 
        # y en la línea 304 en utils.py cambia el  — if parts.netloc: — por — if parts.path: -

    def test_hello_get(self): # Nos regresa 200 cuando hacemos un Get?
        response = self.client.get(url_for('hello'))      
        self.assert200(response)

    def test_hello_post(self): # Se valida el formulario con un Post a Hello?
        fake_form = {
            'username': 'fake-user',
            'password': 'fake-password'
        }
        response = self.client.post(url_for('hello'), data=fake_form)

        self.assertRedirects(response, url_for('index'))