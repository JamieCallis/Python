from rest_framework import viewsets
from .spacy_implimentation.spacyAPI import SpacyAPI
from .serializer import SpacySerializer

'''
    Django rest framework allows you to combine the logic for a set
    of related views into a single Class. Called a Viewset.

    This is the same as Resources of Controllers in other frameworks and
    programming languages.e
'''
class SpacyViewSet(viewsets.ModelViewSet):
    # Create an instance to be used.
    spacyAPI = SpacyAPI()
    serializer_class = SpacySerializer
    # creates a seralizer class that can be used to format the data
    @action(detail=True, methods=['post'], name="query")
    def query(self, request, pk=None):
        serializer_class.setDocument(spacyAPI, request)

    @action(detail=True)
    def queryResult(self, request, pk=None):
        serializer_class.setDocument(spacyAPI)
