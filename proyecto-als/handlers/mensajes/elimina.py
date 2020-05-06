#coding: utf-8
#Elimina mensaje


import webapp2
import time

from model.mensaje import Mensaje

class EliminaMensajeHandler(webapp2.RequestHandler):
    def get(self):
        mensaje = Mensaje.recupera(self.request)
        mensaje.key.delete()
        time.sleep(1)
        return self.redirect("/mensajes/lista?chat="+self.request.GET["chat"])

app = webapp2.WSGIApplication([
    ('/mensajes/elimina', EliminaMensajeHandler)
], debug=True)


