from rest_framework import viewsets
from .spacy_implimentation.spacyAPI import SpacyAPI
from .serializer import SpacySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json

'''
    Django rest framework allows you to combine the logic for a set
    of related views into a single Class. Called a Viewset.

    This is the same as Resources of Controllers in other frameworks and
    programming languages.
'''
class SpacyViewSet(viewsets.ViewSet):
    # Create an instance to be used.
    spacyAPI = SpacyAPI()
    # serializer_class = SpacySerializer
    # creates a seralizer class that can be used to format the data
    @action(detail=False, methods=['POST'], name="query")
    def query(self, request, *args, pk=None):
        serializer = SpacySerializer(data=request.data)
        # JSON is coming through
        print("Request", request.data)
        if serializer.is_valid():
            print(serializer.data['message'])
            #serializer.setDocument(self.spacyAPI, request.data.message)
            #print(serializer.getExplaination(self.spacyAPI))
            return Response({"success": True, "Data": request.data})
        else:
            return Response({"success": False, "Error": "No data"})

    @action(detail=False, name="query-result")
    def queryResult(self, request, pk=None):
        # serializer_class.getExplaination(spacyAPI)
        return Response({"success": True, "Content": "Yay! queryResults"})
