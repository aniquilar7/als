#coding: utf-8
#Nuevo mensaje


import webapp2
import time

from webapp2_extras import jinja2
from google.appengine.ext import ndb
from webapp2_extras.users import users

from model.mensaje import Mensaje

class NuevoMensajeHandler(webapp2.RequestHandler):
    def post(self):
        mensaje = self.request.get("edMensaje", "")
        clave_chat = self.request.GET["chat"]
        usr = users.get_current_user()

        if not(mensaje):
            return self.redirect("/")
        else:
            mensaje = Mensaje(texto=mensaje, estado=False, usuario=usr.email(), clave_chat=ndb.Key(urlsafe=clave_chat))
            mensaje.put()
            time.sleep(1)
            return self.redirect("/mensajes/lista?chat=" + clave_chat)

app = webapp2.WSGIApplication([
    ('/mensajes/nuevo', NuevoMensajeHandler)
], debug=True)


