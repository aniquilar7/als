#coding: utf-8
#Nuevo chat


import webapp2


from webapp2_extras import jinja2


from model.chat import Chat

class NuevoChatHandler(webapp2.RequestHandler):
    def get(self):

        valores_plantilla = {
        }

        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("nuevo_chat.html",
                            **valores_plantilla))

    def post(self):
        self.respone.write("Nuevo chat creado")

app = webapp2.WSGIApplication([
    ('/chats/nuevo', NuevoChatHandler)
], debug=True)


