import webapp2
import jinja2
import os
from Handlers.SesionBase import BaseHandler
import datetime
from google.appengine.ext import db
import json

JINJA_ENVIROMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname('Views/')))

class PrincipalLogin(BaseHandler):
    template = JINJA_ENVIROMENT.get_template('PreguntasAll.html')
    def get(self):
        username = self.session.get('username')
        if username == None:
            self.redirect('/login')
        else:
            template_vars = {
                'title': "Preguntas",
                'titleMenu': "Todas Las Preguntas"
            }
            self.response.write(self.template.render(template_vars))
    def post(self):
        preguntas = []
        descripciones = []
        tags = []
        dateTime = []
        llaves = []

        query = db.GqlQuery("SELECT * FROM Question")
        for i in query:
            preguntas.append(i.question)
            descripciones.append(i.description)
            date = i.date
            dateTime.append(date.strftime("%Y-%m-%d %H:%M:%S"))
            llaves.append(i.key().id())
            searchTP = db.GqlQuery("SELECT * FROM PreguntaTag WHERE idPregunta=:KEY",KEY = i.key())
            tags_separados = []
            for j in searchTP:
                searchT = db.GqlQuery("SELECT * FROM Tag WHERE __key__=:KEY",KEY=j.idTag)
                for k in searchT:
                    tags_separados.append(k.tag)
                tags.append(tags_separados)

        array = {
            'Q':preguntas,
            'D':descripciones,
            'tag':tags,
            'dateT':dateTime,
            'key':llaves
        }
        self.response.out.write(json.dumps(array))
