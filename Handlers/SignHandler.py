import webapp2
import jinja2
import os
from Models.Usuario import Usuario
from google.appengine.ext import db
import hashlib
from Handlers.SesionBase import BaseHandler

JINJA_ENVIROMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname('Views/')))

class Sign(BaseHandler):
    template = JINJA_ENVIROMENT.get_template('Sign.html')
    def get(self):
        username = self.session.get('username')
        if username != None:
            self.redirect('/inicio')
        else:
            template_vars = {
                'title': "Sign In",
                'titleMenu': "Registrate"
            }
            self.response.write(self.template.render(template_vars))

    def post(self):
        username = self.request.get('username',None)
        email = self.request.get('email',None)
        password = self.request.get('pswd',None)

        u = Usuario(email = email,username = username, password = hashlib.sha224(password).hexdigest())
        u.put()
        u.put()

        """print username
        print email
        print password"""

        template_vars = {
            'title': "Sign In",
            'titleMenu': "Registrate"
        }
        self.response.write(self.template.render(template_vars))
