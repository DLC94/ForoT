import webapp2
import jinja2
import os
from Handlers.SesionBase import BaseHandler

JINJA_ENVIROMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname('Views/')))

class PaginaPrincipal(BaseHandler):
    template = JINJA_ENVIROMENT.get_template('Main.html')
    templateIN = JINJA_ENVIROMENT.get_template('MainLogin.html')
    def get(self):
        username = self.session.get('username')
        template_vars = {
            'title': "Bienvenido",
            'titleMenu': "Inicio"
        }

        if username != None:
            #self.redirect('/inicio')
            self.response.write(self.templateIN.render(template_vars))
            self.response.out.write('<div class="container"><div class="col-md-8"><h2>Bienvenido '+username+'</h2></div></div>')
        else:
            self.response.write(self.template.render(template_vars))
