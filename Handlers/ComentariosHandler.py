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

class ComenController(BaseHandler):
    template = JINJA_ENVIROMENT.get_template('MainLogin.html')

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
        com = self.request.get('cmt',None)
        llave = self.request.get('clave',None)
        username = self.request.get('user',None)
        print username
        search = db.GqlQuery("SELECT * FROM Question")
        queryUser = db.GqlQuery("SELECT * FROM Usuario WHERE username=:user",user=username)
        u = queryUser.get()
        k = u.key()

        for i in search:
            if str(i.key().id()) == llave:
                idQ = i.key()
                print i.question
                date_now = datetime.datetime.now()
                c = Comentario(cmt=com,fecha=date_now,pregunta=idQ,correcta = False,user=k)
                c.put()
                c.put()

        self.response.out.write(json.dumps({'message':"listo"}))

    def put(self):
        llave = self.request.get('clave',None)
        #print "Aqui esta la  llave: " + llave
        comentarios = []
        llaves = []
        fechas = []
        usuarios = []
        bestC = []
        bestLL = []
        bestF = []
        bestU = []

        buscaKey = db.GqlQuery("SELECT * FROM Question")
        key = None
        for i in buscaKey:
            idP = str(i.key().id())
            if llave == idP:
                key = i.key()
        for q in db.GqlQuery("SELECT * FROM Comentario WHERE pregunta=:llave AND correcta=False order by fecha",llave=key):
            comentarios.append(q.cmt)
            fechas.append(q.fecha)
            llaves.append(q.key().id())
            usuarios.append(q.user.username)
        for k in db.GqlQuery("SELECT * FROM Comentario WHERE pregunta=:llave AND correcta=True order by fecha",llave=key):
            bestC.append(k.cmt)
            bestF.append(k.fecha)
            bestLL.append(k.key().id())
            bestU.append(k.user.username)
        array = {
            'C':comentarios,
            'LL':llaves,
            'U':usuarios,
            'BK':bestLL,
            'BC':bestC,
            'BU':bestU
            #'dateT':fechas
        }

        self.response.out.write(json.dumps(array))
