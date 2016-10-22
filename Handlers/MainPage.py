import webapp2
import jinja2
import os

JINJA_ENVIROMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname('Views/')))

class PaginaPrincipal(webapp2.RequestHandler):
    template = JINJA_ENVIROMENT.get_template('Main.html')
    def get(self):
        template_vars = {
            'title': "Bienvenido",
            'titleMenu': "Inicio"
        }
        self.response.write(self.template.render(template_vars))
