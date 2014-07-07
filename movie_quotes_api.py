'''
Created on May 29, 2014

The API that our clients will use.

@author: boutell
'''

import endpoints
from protorpc import remote
from models import MovieQuote
import main

@endpoints.api(name="moviequotes", version="v1", description="Movie Quotes API", hostname="boutell-movie-quotes.appspot.com")
class MovieQuotesApi(remote.Service):

    @MovieQuote.method(path="moviequote/insert", http_method="POST", name="moviequote.insert")
    def moviequote_insert(self, request):
        """ Insert a quote """
        if request.from_datastore:
            my_quote = request
        else:
            my_quote = MovieQuote(parent=main.PARENT_KEY, quote=request.quote, movie=request.movie)
        my_quote.put()
        return my_quote
    
    @MovieQuote.query_method(path="moviequote/list", http_method="GET", 
                             name="moviequote.list", query_fields=("limit", "order", "pageToken"))
    def moviequote_list(self, query):
        """ Return all the quotes """
        return query
    
    @MovieQuote.method(request_fields=("entityKey",), path="moviequote/delete/{entityKey}",
                       http_method="DELETE", name="moviequote.delete")
    def moviequote_delete(self, request):
        """ Delete the given quote if present """
        if not request.from_datastore:
            raise endpoints.NotFoundException("movie quote not found")
        request.key.delete()
        return MovieQuote(quote="deleted")
    
app = endpoints.api_server([MovieQuotesApi], restricted=False)


    
