#Chat entre usuarios


from google.appengine.ext import ndb


class Chat(ndb.Model):
    id = ndb.IntegerProperty(required=True)
    usuario1 = ndb.String(indexed=True)
    usuario2 = ndb.StringProperty(indexed=True)
