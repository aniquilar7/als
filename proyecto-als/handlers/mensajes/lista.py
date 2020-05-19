import webapp2
from webapp2_extras import jinja2

from webapp2_extras.users import users
from model.mensaje import Mensaje

class ListaMensajesHandler(webapp2.RequestHandler):
    def get(self):
        url_usr = users.create_logout_url("/")

        chat, mensajes = Mensaje.recupera_para(self.request)

        valores_plantilla = {
            "mensajes": mensajes,
            "chat": chat,
            "url_usr": url_usr
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("lista_mensajes.html",
                            **valores_plantilla))

app = webapp2.WSGIApplication([
    ('/mensajes/lista', ListaMensajesHandler)
], debug=True)
