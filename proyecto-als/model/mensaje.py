#Mensaje enviado por un usuario


from google.appengine.ext import ndb

from chat import Chat

class Mensaje(ndb.Model):
    fecha = ndb.DateTimeProperty(auto_now_add=True, indexed=True)
    texto = ndb.StringProperty(required=True)
    estado = ndb.BooleanProperty(required=True)
    usuario = ndb.StringProperty(required=True)
    clave_chat = ndb.KeyProperty(kind=Chat)

    @staticmethod
    def recupera_para(req):
        try:
            id_chat = req.GET["chat"]
        except:
            id_chat = ""

        if id_chat:
            clave_chat = ndb.Key(urlsafe=id_chat)
            mensajes = Mensaje.query(Mensaje.clave_chat == clave_chat).order(Mensaje.fecha)
            return (clave_chat.get(), mensajes)
        else:
            print ("ERROR: chat no encontrado")

    @staticmethod
    def recupera(req):
        try:
            id = req.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()