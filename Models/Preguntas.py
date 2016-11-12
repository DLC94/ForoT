import datetime
from google.appengine.ext import db
from Models.Usuario import Usuario

class Question(db.Model):
    question = db.StringProperty()
    description = db.TextProperty()
    date = db.DateTimeProperty()
    usuario = db.ReferenceProperty(Usuario)
    respuesta = db.BooleanProperty()
