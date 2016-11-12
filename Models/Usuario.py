from google.appengine.ext import db

class Usuario(db.Model):
    email = db.StringProperty();
    username = db.StringProperty();
    password = db.StringProperty();
