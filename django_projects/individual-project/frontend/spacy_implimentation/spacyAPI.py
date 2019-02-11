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
        for word in self.doc.ents:
            newDict = dict(word=word.text, explained=word.label_)
            ItemList.append(newDict)
        
        return ItemList

