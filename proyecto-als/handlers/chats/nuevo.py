#coding: utf-8
#Nuevo chat


import webapp2
import time

from webapp2_extras import jinja2
from webapp2_extras.users import users


from model.chat import Chat

class NuevoChatHandler(webapp2.RequestHandler):
    def get(self):

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("nuevo_chat.html"))

    def post(self):
        usr = users.get_current_user()
        usuario = self.request.get("edUsuario", "")

        if not(usuario):
            return self.redirect("/inicio")
        else:
            chat = Chat(usuario1=usr.email(), usuario2=usuario)
            chat.put()
            time.sleep(1)
            return self.redirect("/inicio")

app = webapp2.WSGIApplication([
    ('/chats/nuevo', NuevoChatHandler)
], debug=True)


