#Chat entre usuarios


from google.appengine.ext import ndb


class Chat(ndb.Model):
    usuario1 = ndb.StringProperty(indexed=True)
    usuario2 = ndb.StringProperty(indexed=True)
