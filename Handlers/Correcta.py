import webapp2
import jinja2
import os
import json
import datetime
from Models.Preguntas import Question
from Models.Comentario import Comentario
from google.appengine.ext import db
from Handlers.SesionBase import BaseHandler

JINJA_ENVIROMENT = jinja2.Environment(loader = jinja2.FileSystemLoader(os.path.dirname('Views/')))

class CorController(BaseHandler):
    template = JINJA_ENVIROMENT.get_template('MainLogin.html')

    def get(self):
        username = self.session.get('username')
        if username == None:
            self.redirect('/login')
        else:
            self.redirect('/inicio')

    def post(self):
        idQ = self.request.get('idQ',None)
        idC = self.request.get('LL',None)

        query = db.GqlQuery("SELECT * FROM Question")
        for i in query:
            if idQ == str(i.key().id()):
                print i.question
                i.respuesta = True
                i.put()
                for j in db.GqlQuery("SELECT * FROM Comentario WHERE pregunta=:key",key=i.key()):
                    if idC == str(j.key().id()):
                        j.correcta = True
                        j.put()
                    else:
                        j.correcta = False
                        j.put()
        self.response.out.write(json.dumps({'message':"listo"}))

    def put(self):
        qID = self.request.get('idQ',None)
        cID = self.request.get('LL',None)

        query = db.GqlQuery("SELECT * FROM Question")
        for i in query:
            if qID == str(i.key().id()):
                i.respuesta = False
                i.put()
                for j in db.GqlQuery("SELECT * FROM Comentario WHERE pregunta=:key",key=i.key()):
                    if cID == str(j.key().id()):
                        j.correcta = False
                        j.put()
        self.response.out.write(json.dumps({'message':'listo'}))
