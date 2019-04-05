from rest_framework import serializers

from .models import BookMetaData, BookText
import json
'''
    We make use of a seralizer from the rest_framework
    to allow us to transform the data into JSON or XML format.

    Seralizer allows us to put data into native python datatypes,
    that can be easily rendered into other content types.
'''


class SpacySerializer(serializers.Serializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        context = kwargs.get('context', None)

        if context:
            request = kwargs['context']['request']

    def getSentence(self):
        return self.context['request']['message']

    def setDocument(self, instance, sentence):
        self.sentence = sentence
        instance.createDoc(self.sentence)

    def getExplaination(self, instance):
        instance.explainDoc()


class BookMetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMetaData
        fields = '__all__'
           
class BookTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookText
        fields = '__all__'

 
    
    