from rest_framework import viewsets
from .spacy_implimentation.spacyAPI import SpacyAPI
from .serializer import SpacySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers

'''
    Django rest framework allows you to combine the logic for a set
    of related views into a single Class. Called a Viewset.

    This is the same as Resources of Controllers in other frameworks and
    programming languages.e
'''
class SpacyViewSet(viewsets.ViewSet):
    # Create an instance to be used.

    spacyAPI = SpacyAPI()
    serializer_class = SpacySerializer
    # creates a seralizer class that can be used to format the data
    @action(detail=True, methods=['POST', 'GET'], url_path="query", url_name="query")
    def query(self, request, pk=None):
        # serializer_class.setDocument(spacyAPI, request)
        print(request)
        return Response({"success": True, "Content": "Yay! query"})

    @action(detail=True, name="query-result", url_path="query-result", url_name="query-result")
    def queryResult(self, request, pk=None):
        # serializer_class.getExplaination(spacyAPI)
        return Response({"success": True, "Content": "Yay! queryResults"})
