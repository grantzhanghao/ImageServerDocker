from rest_framework.response  import Response
from rest_framework.request  import Request
from rest_framework.renderers import JSONRenderer
from io import BytesIO
from django.http import HttpResponse,HttpRequest
import os
import pickle
from datetime import datetime
from datetime import timedelta
from api.drawgraphs.mock_graph import draw_mock_graph
from urllib.parse import urlparse, parse_qs
from .view import KMCGraph

class MockPicture(KMCGraph):
    def get(self, request, format=None):
        
        parameters ={'locale':'en'}
        return self.draw_graph(parameters)
    
    def draw_graph(self, parameters, isdebug = False):
        
        pil_image = draw_mock_graph()

        response = HttpResponse(content_type="image/png")
        pil_image.save(response,"PNG")

        return response

    def debug_graph(self, url):
        
        parameters = {'locale':'en'}
        return self.draw_graph(parameters, True)
