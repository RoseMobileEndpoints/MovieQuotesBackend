'''
Created on May 21, 2014

@author: boutell
'''

from endpoints_proto_datastore.ndb.model import EndpointsModel
from google.appengine.ext import ndb

class MovieQuote(EndpointsModel):
    """ A movie quote and the title of the movie from which it came """
    _message_fields_schema = ("entityKey", "quote", "movie", "last_touch_date_time")
    quote = ndb.StringProperty()
    movie = ndb.StringProperty()
    last_touch_date_time = ndb.DateTimeProperty(auto_now=True)
    

