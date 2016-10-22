from google.appengine.ext import db
from Models.Preguntas import Question
from Models.Tag import Tag

class PreguntaTag(db.Model):
    #idPregunta = db.IntegerProperty()
    #idTag = db.IntegerProperty()
    idPregunta = db.ReferenceProperty(Question)
    idTag = db.ReferenceProperty(Tag)
