import webapp2
import jinja2
import os
from Handlers.SesionBase import BaseHandler

JINJA_ENVIROMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname('Views/')))

class logout(BaseHandler):
    template = JINJA_ENVIROMENT.get_template('Main.html')
    def get(self):
        self.session.clear()
        self.redirect('/')
