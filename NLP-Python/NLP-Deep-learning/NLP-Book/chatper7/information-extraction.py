import nltk, re, pprint
from nltk.corpus import conll2000

def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences

doc = """
The fourth Wells account moving to another agency is the packaged
paper-products division of Georgia-Pasific Corp., which
arrived at Wells only last fall. Like Hertz and the History Channel,
it is also leaving for an Omnicom-owned agency, the BBDO South unit of BBDO
Wordwide. BBDO South in Atlanta, which handles corporate advertising
for Georgia-Pacific, will assume additional duties for brands
like Angel Soft toilet tissue and Sparkle paper towels, siad
Ken Haldin, a spokesman for Georgia-Pacific in Atlanta.
"""


sentences = ie_preprocess(doc)
#print sentences[0]

grammar = r"NP: {<DT>?<JJ>*<NN>}"

cp = nltk.RegexpParser(grammar)
result = cp.parse(sentences[0])
#print result
# draws a tree image containing the sentence structures
#result.draw()

# Simple Noun Phrase Chunker

grammar = r"""
    NP: {<DT\$>?<JJ>*<NN>}  # chunk determiner / possessive, adjectives and noun
        {<NNP>+}            # chunk sequences of proper nouns
"""
# If pattern matches at overlapping locations, the leftmost match
# takes precedence.
cp = nltk.RegexpParser(grammar)
#print cp.parse(sentences[0])

# Exploring Test Corpora
# cp = nltk.RegexpParser('CHUNK: {<V.*> <TO> <V.*>}')
# brown = nltk.corpus.brown
# for sent in brown.tagged_sents():
#     tree = cp.parse(sent)
#     for subtree in tree.subtrees():
#         if subtree.label() == 'CHUNK': print(subtree)

# chinking

'''
    Is the process of excluding from a chunk. 
    It's a sequence of tokens that is not included in
    a chunk.
'''

grammar = r"""
    NP:
    {<.*>+} # chunk everything
    }<NN|NNP>+{ # Chink sequqences of VBD and IN
"""

cp = nltk.RegexpParser(grammar)
print cp.parse(sentences[0])

# class UnigramChunker(nltk.ChunkParserI):
#     def __init__(self, train_sents):
#         train_data = [[(t,c) for w,t,c in 
#                     nltk.chunk.tree2conlltags(sent)]
#                     for sent in train_sents]
#         self.tagger = nltk.UnigramTagger(train_data)
    
#     def parse(self, sentence):
#         pos_tags = [pos for (word, pos) in sentence]
#         tagged_pos_tags = self.tagger.tag(pos_tags)
#         chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
#         conlltags = [(word, pos, chunktag) for ((word, pos), chunktag)
#                     in zip(sentence, chunktags)]
#         return nltk.chunk.conlltags2tree(conlltags)

# Constructor expects a list of training setences,
# which will be in the form of chunk trees.

# test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
# train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
# unigram_chunker = UnigramChunker(train_sents)
# print unigram_chunker.evaluate(test_sents)

# postags = sorted(set(pos for sent in train_sents
#                 for (word, pos) in sent.leaves()))

# print(unigram_chunker.tagger.tag(postags))

def npchunk_features(sentence, i, history):
    word, pos = sentence[i]
    return {"pos": pos}

class ConsecutiveNPChunkTagger(nltk.TaggerI):
    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = npchunk_features(untagged_sent, i, history)
                train_set.append( (featureset, tag) )
                history.append(tag)
        self.classifier = nltk.MaxentClassifier.train( 
            train_set, algorithm='megam', trace=0)

    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            featureset = npchunk_features(sentence, i, history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence, history)

class ConsecutiveNPChunker(nltk.ChunkParserI): 
    def __init__(self, train_sents):
        tagged_sents = [[((w,t),c) for (w,t,c) in
                         nltk.chunk.tree2conlltags(sent)]
                        for sent in train_sents]
        self.tagger = ConsecutiveNPChunkTagger(tagged_sents)

    def parse(self, sentence):
        tagged_sents = self.tagger.tag(sentence)
        conlltags = [(w,t,c) for ((w,t),c) in tagged_sents]
        return nltk.chunk.conlltags2tree(conlltags)

test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
chunker = ConsecutiveNPChunker(train_sents)
print(chunker.evaluate(test_sents))
