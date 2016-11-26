from google.appengine.ext import db
from Models.Tag import Tag
class TagD(Tag):
    #los atributos de tag estan aqui
    fecha = db.DateTimeProperty()
