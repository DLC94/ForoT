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

def esta_repetido(strQuery,elemento):
    search = db.GqlQuery(strQuery)
    for j in search:
        if j.tag == elemento:
            return True
    return False


class QuestionHandler(BaseHandler):
    template = JINJA_ENVIROMENT.get_template('Preguntas.html')
    def get(self):
        username = self.session.get('username')
        if username == None:
            self.redirect('/login')
        else:
            template_vars = {
                'title': "Subir Pregunta",
                'titleMenu': "Sube una Pregunta"
            }
            self.response.write(self.template.render(template_vars))


    def post(self):
        titulo = self.request.get("question",None)
        description = self.request.get("description",None)
        msj = self.request.get_all("tag",None)
        date_now = datetime.datetime.now()
        username = self.session.get('username')

        query = db.GqlQuery("SELECT * FROM Usuario WHERE username=:user",user=username)
        k = query.get()
        key = k.key()

        q = Question(question = titulo,description = description,date = date_now, usuario = key, respuesta = False)
        q.put()
        q.put()

        lista = msj[0].split(',')
        for i in lista:
            if esta_repetido("SELECT * FROM Tag",i):
                search = db.GqlQuery("SELECT * FROM Tag WHERE tag=:TAG",TAG=i)
                tagE = search.get()#regresa solo uno
                key = tagE.key()
                pt = PTAG(idPregunta=q,idTag=key)
                pt.put()
                pt.put()
            else:
                t = Tag(tag = i)
                t.put()
                t.put()
                pt = PTAG(idPregunta=q,idTag=t)
                pt.put()
                pt.put()

        self.response.out.write(json.dumps({'message':titulo}))

    def put(self):
        search = db.GqlQuery("SELECT * FROM Tag")
        tags = []
        for i in search:
            tags.append(i.tag)
        array = {
            'tag':tags,
            'error':'Ya valiste valedor'
        }
        self.response.write(json.dumps(array))
