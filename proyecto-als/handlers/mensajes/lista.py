import webapp2
from webapp2_extras import jinja2
import time

from webapp2_extras.users import users
from model.mensaje import Mensaje

class ListaMensajesHandler(webapp2.RequestHandler):
    def get(self):
        url_usr = users.create_logout_url("/")

        chat, mensajes = Mensaje.recupera_para(self.request)

        for mensaje in mensajes:
            if mensaje.usuario != users.get_current_user().email():
                mensaje.estado = True
                mensaje.put()
        time.sleep(1)

        if chat.usuario1 == users.get_current_user().email():
            usr = chat.usuario2
        elif chat.usuario2 == users.get_current_user().email():
            usr = chat.usuario1

        valores_plantilla = {
            "mensajes": mensajes,
            "chat": chat,
            "url_usr": url_usr,
            "usr": usr
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("lista_mensajes.html",
                            **valores_plantilla))

app = webapp2.WSGIApplication([
    ('/mensajes/lista', ListaMensajesHandler)
], debug=True)
