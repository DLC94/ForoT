import webapp2
import jinja2
import os
import json
import datetime
from Models.Preguntas import Question
from Models.Comentario import Comentario
from google.appengine.ext import db

JINJA_ENVIROMENT = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.dirname('Views/')))

class ComenController(webapp2.RequestHandler):
    template = JINJA_ENVIROMENT.get_template('Main.html')

    def get(self):
        template_vars = {
            'title': "Subir Pregunta",
            'titleMenu': "Sube una Pregunta"
        }
        self.response.write(self.template.render(template_vars))

    def post(self):
        com = self.request.get('cmt',None)
        llave = self.request.get('clave',None)
        print com
        print "Llave recibida" + llave
        search = db.GqlQuery("SELECT * FROM Question")
        for i in search:
            idP = str(i.key().id())
            print "La id es: " + idP
            if idP == llave:
                idQ = i.key()
        date_now = datetime.datetime.now()
        c = Comentario(cmt=com,fecha=date_now,pregunta=idQ)
        c.put()
        c.put()

        self.response.out.write(json.dumps({'message':"listo"}))
