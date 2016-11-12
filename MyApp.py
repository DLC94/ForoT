import webapp2
import jinja2
import os
from Handlers.PreguntaHandler import QuestionHandler as QH
from Handlers.MostrarHandler import MostrarQ as MQ
from Handlers.MainPage import PaginaPrincipal as MP
from Handlers.TagHandler import TControlle as TC
from Handlers.ComentariosHandler import ComenController
from Handlers.SignHandler import Sign as S
from Handlers.LogHandler import Log as L
from Handlers.MainLogin import PrincipalLogin as PL
from Handlers.DestroySession import logout as LO
from Handlers.Correcta import CorController


config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}

app = webapp2.WSGIApplication([
    ('/',MP),
    ('/pregunta',QH),
    ('/tuspreguntas',MQ),
    ('/tag',TC),
    ('/comentarios',ComenController),
    ('/signin',S),
    ('/login',L),
    ('/inicio',PL),
    ('/logout',LO),
    ('/cambia',CorController),
],config=config,
debug = True)
