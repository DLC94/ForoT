import webapp2
import jinja2
import os
import json
from Models.Preguntas import Question
from Models.Tag import Tag
from Models.PreguntaTag import PreguntaTag
import datetime
from google.appengine.ext import db

JINJA_ENVIRONMENT = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.dirname("Views/")))

class MostrarQ(webapp2.RequestHandler):
    template = JINJA_ENVIRONMENT.get_template('MostrarPre.html')

    def get(self):
        template_var = {
            'title': "Tus Preguntas",
            'titleMenu': "Preguntas que haz realizado"
        }
        self.response.write(self.template.render(template_var))

    def post(self):
        preguntas = []
        descripciones = []
        tags = []
        dateTime = []
        llaves = []
        idQuestion = None
        idT = None

        searchQ = db.GqlQuery("SELECT * FROM Question order by date Desc",)#Busca todas preguntas
        for i in searchQ:
            #idQuestion = i.key().id()
            preguntas.append(i.question)
            descripciones.append(i.description)
            date = i.date
            dateTime.append(date.strftime("%Y-%m-%d %H:%M:%S"))
            llaves.append(i.key().id())
            searchTP = db.GqlQuery("SELECT * FROM PreguntaTag WHERE idPregunta=:KEY",KEY=i.key())
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
            'key':llaves,
            'error':"Ya valiste valedor"
        }
        self.response.out.write(json.dumps(array))

    def put(self):
        com = self.request.get('cmt',None)
        llave = self.request.get('clave',None)

        #search = db.GqlQuery("SELECT * FROM Question")
        #for i in search:
        #    if llave == i.key().id():
        #        idP = i
        #date_now = datetime.datetime.now()
        #c = Comentario(cmt=com,fecha=date_now,pregunta=idP.key())

        #self.response.out.write(json.dumps({'message':"listo"}))
