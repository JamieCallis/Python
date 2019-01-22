from rest_framework import serializers


'''
    We make use of a seralizer from the rest_framework
    to allow us to transform the data into JSON or XML format.

    Seralizer allows us to put data into native python datatypes,
    that can be easily rendered into other content types.
'''
class SpacySerializer(serializers.Serializer):
    def setDocument(instance, sentence):
        instance.createDoc(sentence)

    def getExplaination(instance):
        instance.explainDoc()
