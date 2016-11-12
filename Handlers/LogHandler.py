import webapp2
import jinja2
import os
from google.appengine.ext import db
from Models.Usuario import Usuario
import hashlib
from Handlers.SesionBase import BaseHandler

JINJA_ENVIROMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname('Views/')))

class Log(BaseHandler):
    template = JINJA_ENVIROMENT.get_template('Log.html')
    def get(self):
        username = self.session.get('username')
        if username != None:
            self.redirect('/inicio')
        else:
            template_vars = {
                'title': "Log In",
                'titleMenu': "Inicia Sesion"
            }
            self.response.write(self.template.render(template_vars))

    def post(self):
        noExiste = False
        incorrecto = False
        email = self.request.get('email',None)
        password = self.request.get('pswd',None)
        p = hashlib.sha224(password).hexdigest()

        u = db.GqlQuery("SELECT * FROM Usuario WHERE email=:correo",correo=email)
        user = u.get()

        if user == None:
            noExiste = True
        else:
            if user.password == p:
                self.session['username'] = user.username
                self.redirect('/inicio')
            else:
                incorrecto = True


        template_vars = {
            'title': "Log In",
            'titleMenu': "Inicia Sesion"
        }
        self.response.write(self.template.render(template_vars))
        if noExiste == True:
            self.response.out.write('<div class="container"><div class="col-md-8 text-left"><h5 style="color:red">*Correo Incorrecto.</h5></div></div>')
        if incorrecto == True:
            self.response.out.write('<div class="container"><div class="col-md-8 text-left"><h5 style="color:red">*Contrase&ntilde;a incorrecta.</h5></div></div>')
