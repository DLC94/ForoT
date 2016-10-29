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
        print "Esto es prueba" + llave
        print "Esot es el comentario" + com
        search = db.GqlQuery("SELECT * FROM Question")
        for i in search:

            if str(i.key().id()) == llave:
                idQ = i.key()
                print i.question
                date_now = datetime.datetime.now()
                c = Comentario(cmt=com,fecha=date_now,pregunta=idQ)
                c.put()
                c.put()

        self.response.out.write(json.dumps({'message':"listo"}))

    def put(self):
        llave = self.request.get('clave',None)
        #print "Aqui esta la  llave: " + llave
        comentarios = []
        fechas = []

        buscaKey = db.GqlQuery("SELECT * FROM Question")
        key = None
        for i in buscaKey:
            idP = str(i.key().id())
            if llave == idP:
                key = i.key()
        print key
        for q in db.GqlQuery("SELECT * FROM Comentario WHERE pregunta=:llave",llave=key):
            comentarios.append(q.cmt)
            fechas.append(q.fecha)
        array = {
            'C':comentarios,
            #'dateT':fechas
        }

        self.response.out.write(json.dumps(array))
