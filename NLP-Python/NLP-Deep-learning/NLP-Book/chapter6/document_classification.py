import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import brown

# building dataset
# documents = [(list(movie_reviews.words(fileid)), category)
#             for category in movie_reviews.categories()
#             for fileid in movie_reviews.fileids(category)]
# random.shuffle(documents)

# building the feature extractor
# all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
# word_features = list(all_words)[:2000]

'''
    The reason that we compute the set of all words in a document in,
    rather than just checking if word in document, is that checking
    whether a word occurs in a set is much faster than checking whether it
    occurs in a list.
'''
def document_features(documents):
    document_words = set(documents)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

# print(document_features(movie_reviews.words('pos/cv957_8737.txt')))

# featuresets = [(document_features(d), c) for (d,c) in documents]
# train_set, test_set = featuresets[100:], featuresets[:100]
# classifier = nltk.NaiveBayesClassifier.train(train_set)

# print (nltk.classify.accuracy(classifier, test_set))

# print classifier.show_most_informative_features(5)

# training a classifier to work out which suffixes are most
# informative.

# suffix_fdist = nltk.FreqDist()

# for word in brown.words():
#     word = word.lower()
#     suffix_fdist[word[-1:]] += 1
#     suffix_fdist[word[-2:]] += 1
#     suffix_fdist[word[-3:]] += 1

# common_suffixes = [suffix for (suffix, count) in suffix_fdist.most_common(100)]

'''
    A part-of-speech classifier whose feature dector examines the context
    in which a word appears in order to determine which part of speech
    tag should be assigned. In particular, the identiy of the previous
    word is included as a feature.

    Sequence classification strategy, known as 'consecutive classification'
    or 'greedy sequence classification'.

    Makes use of a history arguement looking to the left of a word,
    which has already been tagged. Such creating colloation between
    words.
'''


def pos_features(sentence, i, history):
    features = {
        "suffix(1)": sentence[i][-1:],
        "suffix(2)": sentence[i][-2:],
        "suffix(3)": sentence[i][-3:]
    }
    if i == 0:
        features["prev-word"] = "<START>"
        features["prev-tag"] = "<START>"
    else:
        features["prev-word"] = sentence[i-1]
        features["prev-tag"] = history[i-1]
    return features

class ConsecutivePosTagger(nltk.TaggerI):
    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            untagged_sent = nltk.tag.untag(tagged_sent)
            history = []
            for i, (word, tag) in enumerate(tagged_sent):
                featureset = pos_features(untagged_sent, i, history)
                train_set.append((featureset, tag))
                history.append(tag)
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)
    
    def tag(self, sentence):
        history = []
        for i, word in enumerate(sentence):
            freatureset = pos_features(sentence, i, history)
            tag = self.classifier.classify(freatureset)
            history.append(tag)
        return zip(sentence, history)


tagged_sents = brown.tagged_sents(categories='news')
size = int(len(tagged_sents) * 0.1)

train_sents, test_sents = tagged_sents[size:], tagged_sents[:size]
tagger = ConsecutivePosTagger(train_sents)
print tagger.evaluate(test_sents)
