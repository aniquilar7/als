#Mensaje enviado por un usuario


from google.appengine.ext import ndb

from chat import Chat

class Mensaje(ndb.Model):
    fecha = ndb.DateTimeProperty(auto_now_add=True, indexed=True)
    texto = ndb.StringProperty(required=True)
    estado = ndb.BooleanProperty(required=True)
    chat = ndb.KeyProperty(kind=Chat)
