#coding: utf-8
#Elimina chat


import webapp2
import time

from model.chat import Chat

class EliminaChatHandler(webapp2.RequestHandler):
    def get(self):
        chat = Chat.recupera(self.request)
        chat.key.delete()
        time.sleep(1)
        return self.redirect("/inicio")

app = webapp2.WSGIApplication([
    ('/chats/elimina', EliminaChatHandler)
], debug=True)


