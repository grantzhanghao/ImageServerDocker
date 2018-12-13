from rest_framework.views import APIView

class KMCGraph(APIView):
    '''
        Base class for creating graph.
    '''
    def get(self, request, format=None):
        '''
            draw the graph and return a image response.
        '''
    
    def draw_graph(self, parameters, isdebug = False):
        '''
            parameters is a dictionary. one parameter will always be locale that defaults to 'en'.
            draw the graph and return a image response.
        '''

    def debug_graph(self, url):
        '''
            It is uesed to debug locally. It takes a url and calls the draw_graph method with the parameters from the url.
        '''