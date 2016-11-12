import webapp2
import jinja2
import os
import json
from Models.Preguntas import Question
from Models.Tag import Tag
from Models.PreguntaTag import PreguntaTag as PTAG
from google.appengine.ext import db
import datetime
from Handlers.SesionBase import BaseHandler

JINJA_ENVIROMENT = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.dirname('Views/')))

class TControlle(BaseHandler):
    template = JINJA_ENVIROMENT.get_template('Tags.html')

    def get(self):
        username = self.session.get('username')
        if username == None:
            self.redirect('/login')
        else:
            tag = self.request.get("TagSeleccionado",None)

            dateTime = []
            description = []
            question = []
            d = []

            tags = db.GqlQuery("SELECT __key__ FROM Tag WHERE tag=:t",t=tag)
            idT = tags.get()
            idpreguntas = db.GqlQuery("SELECT idPregunta FROM PreguntaTag WHERE idTag=:idT",idT=idT)
            for i in idpreguntas:
                pregunta = db.GqlQuery("SELECT * FROM Question WHERE __key__=:idQuestion",idQuestion=i.idPregunta)
                for j in pregunta:
                    question.append(j.question)
                    description.append(j.description)
                    date = j.date
                    dateTime.append(date.strftime("%Y-%m-%d %H:%M:%S"))
            print dateTime
            tam = len(question)
            for j in range(0,tam):
                u = {
                    'q':question[j],
                    'd':description[j],
                    'dateT':dateTime[j]
                }
                d.append(u)
            template_vars = {
                'title': "Tags",
                'titleMenu': "Preguntas Relacionadas",
                'Saludo':tag,
                'Preguntas':d
            }
            self.response.write(self.template.render(template_vars))
