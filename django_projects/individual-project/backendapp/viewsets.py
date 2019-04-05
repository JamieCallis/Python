from rest_framework import viewsets, filters
from .spacy_implimentation.spacyAPI import SpacyAPI
from .text_summarization.summarization import Summarization
from .serializer import SpacySerializer, BookMetaDataSerializer, BookTextSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import serializers, permissions
from rest_framework.views import APIView
from rest_framework import pagination
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import status
import json

from .models import BookMetaData, BookText

'''
    Django rest framework allows you to combine the logic for a set
    of related views into a single Class. Called a Viewset.

    This is the same as Resources of Controllers in other frameworks and
    programming languages.
'''

class SpacyViewSet(viewsets.ViewSet):
    # Create an instance to be used.
    # need to sort out authentification with this section. 
    @action(detail=True, methods=['POST'], name="query", description="Serializes the data, and returns a processed result")
    def query(self, request, *args, pk=None):
        spacyAPI = SpacyAPI()
        spacySerializer = SpacySerializer(args, context={"request": request.data})
        spacyAPI.createDoc(spacySerializer.getSentence())

        return Response({"success": True, "result": spacyAPI.explainDoc()})

'''
    # A model view set requires a queryset and a serializer_class
    # Since we only want the user to be able to get records and not edit
    # we need to use the read only model view set. 
    # Along with token authentification will give us enough security.
'''
class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_parama='page_size'

    def get_paginated_response(self, data):
        # print(data)
        context = {
        'next': self.get_next_link(),
        'previous': self.get_previous_link(),
        'count': self.page.paginator.count,
        'results': data,
        }

        return Response(context)


class BookMetaDataViewSet(viewsets.ModelViewSet):
    queryset = BookMetaData.objects.all().order_by('bookID')
    serializer_class = BookMetaDataSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = (filters.SearchFilter,)
    search_fields= ('title', 'author', 'subjects')

    def  get_queryset(self):
        queryset = BookMetaData.objects.all().order_by('bookID')
        return queryset

    @action(detail=False, methods=['GET'], name="book-subject", description="Gather the books")
    def getBooksSubject(self, request, *args, pk=None):
        bookID = self.request.query_params.get('bookID', None)
        if bookID is not None:
            # no matter where what the item is we will get the correct information for subject
            # meaning we can correctly build the results
            subjects = BookMetaData.objects.values('subjects').get(bookID=bookID)
            subjects = subjects['subjects']
            subjects = subjects.decode()
            subjects = json.loads(subjects)
            print(subjects)
            return Response(subjects, status=200)
        return Response(status=400)
   
        

   
class BookTextViewSet(viewsets.ModelViewSet):
    # filters based on the bookID since every row has a unique bookID attached to it
    # as a foreign key, and we will be using this are the filtering criteria.
    queryset = BookText.objects.all()
    serializer_class = BookTextSerializer
    
    @action(detail=False, methods=['GET'], name="book-query", description="grab individual book information, based on bookID")
    def bookDetailsQuery(self, request, *args, pk=None):
        queryset = BookText.objects.all()
        bookID = self.request.query_params.get('bookID', None)
        if bookID is not None:
            queryset = queryset.filter(bookID_id=bookID)
            textSummary = Summarization(queryset[0].bookContents)
            return Response({"id": queryset[0].id, "bookContents": textSummary.getOringalText(), "bookSummary": textSummary.getTextSummarization(), "bookID": bookID})
        return Response(status=400)
