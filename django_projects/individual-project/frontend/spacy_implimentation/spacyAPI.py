import spacy



class SpacyAPI(object):
    nlp = None
    doc = None
    explainList = []
    # constructor
    def __init__(self):
        # create a English module that can be used throughout the class.
        self.nlp = spacy.load('en_core_web_sm')

    def createDoc(sentence):
        self.doc = self.nlp(setence)
    # how can we adapt this so it can return a suitible type.
    def explainDoc():
        for word in self.doc:
            print(word.text, word.tag_, spacy.explain(word.tag_))