import spacy

class SpacyAPI(object):
    explainList = []
    # constructor
    def __init__(self):
        # create a English module that can be used throughout the class.
        self.nlp = spacy.load('en_core_web_sm')
        self.doc = None

    def createDoc(self,sentence):
        self.doc = self.nlp(sentence)
        return self.doc
    # how can we adapt this so it can return a suitible type.
    def explainDoc(self):
        ItemList = []
        for token in self.doc:
            newDict = dict(word=token.text, pos=token.pos_,pos_responsing=spacy.explain(token.pos_))
            ItemList.append(newDict)
        
        return ItemList

