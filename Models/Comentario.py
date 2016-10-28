from google.appengine.ext import db
from Models.Preguntas import Question

class Comentario(db.Model):
    cmt = db.StringProperty();
    fecha = db.DateTimeProperty();
    pregunta = db.ReferenceProperty(Question)
