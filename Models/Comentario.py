from google.appengine.ext import db
from Models.Preguntas import Question

class Comentario(db.Model):
    cmt = db.TextProperty();
    fecha = db.DateTimeProperty();
    correcta = db.BooleanProperty();
    pregunta = db.ReferenceProperty(Question)
