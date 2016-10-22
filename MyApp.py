import webapp2
import jinja2
import os
from Handlers.PreguntaHandler import QuestionHandler as QH
from Handlers.MostrarHandler import MostrarQ as MQ
from Handlers.MainPage import PaginaPrincipal as MP
from Handlers.TagHandler import TControlle as TC


app = webapp2.WSGIApplication([
    ('/',MP),
    ('/pregunta',QH),
    ('/tuspreguntas',MQ),
    ('/tag',TC)
],debug = True)
