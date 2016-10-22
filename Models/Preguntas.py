import datetime
from google.appengine.ext import db

class Question(db.Model):
    question = db.StringProperty()
    description = db.TextProperty()
    date = db.DateTimeProperty()
