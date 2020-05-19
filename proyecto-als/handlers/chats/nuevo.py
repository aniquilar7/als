#coding: utf-8
#Nuevo chat


import webapp2
import time

from webapp2_extras import jinja2


from model.chat import Chat

class NuevoChatHandler(webapp2.RequestHandler):
    def get(self):


        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("nuevo_chat.html"))

    def post(self):
        usuario = self.request.get("edUsuario", "")

        if not(usuario):
            return self.redirect("/inicio")
        else:
            chat = Chat(usuario1="Yo", usuario2=usuario)
            chat.put()
            time.sleep(1)
            return self.redirect("/inicio")

app = webapp2.WSGIApplication([
    ('/chats/nuevo', NuevoChatHandler)
], debug=True)


