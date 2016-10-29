from google.appengine.ext import db
from Models.Preguntas import Question

class Comentario(db.Model):
    cmt = db.TextProperty();
    fecha = db.DateTimeProperty();
    pregunta = db.ReferenceProperty(Question)
