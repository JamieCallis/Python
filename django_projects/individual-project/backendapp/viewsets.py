from rest_framework import viewsets
from .spacy_implimentation.spacyAPI import SpacyAPI
from .serializer import SpacySerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
import io

'''
    Django rest framework allows you to combine the logic for a set
    of related views into a single Class. Called a Viewset.

    This is the same as Resources of Controllers in other frameworks and
    programming languages.
'''


class SpacyViewSet(viewsets.ViewSet):
    # Create an instance to be used.

    @action(detail=False, methods=['POST'], name="query", description="Serializes the data, and returns a processed result")
    def query(self, request, *args, pk=None):
        spacyAPI = SpacyAPI()
        spacySerializer = SpacySerializer(args, context={"request": request.data})
        spacyAPI.createDoc(spacySerializer.getSentence())

        return Response({"success": True, "result": spacyAPI.explainDoc()})


    @action(detail=False, name="queryresult")
    def queryResult(self, request, pk=None):
        return Response({"success": True, "Content": "working"})

    
