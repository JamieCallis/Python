import nltk
import random
from nltk.corpus import movie_reviews
from nltk.corpus import brown

# building dataset
documents = [(list(movie_reviews.words(fileid)), category)
            for category in movie_reviews.categories()
            for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)

# building the feature extractor
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
word_features = list(all_words)[:2000]

'''
    The reason that we compute teh set of all words in a document in,
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

suffix_fdist = nltk.FreqDist()

for word in brown.words():
    word = word.lower()
    suffix_fdist[word[-1:]] += 1
    suffix_fdist[word[-2:]] += 1
    suffix_fdist[word[-3:]] += 1

common_suffixes = [suffix for (suffix, count) in suffix_fdist.most_common(100)]
print common_suffixes

def pos_features(word):
    features = {}
    for suffix in common_suffixes:
        features['endswith({})'.format(suffix)] = word.lower().endswith(suffix)
    return features

tagged_words = brown.tagged_words(categories='news')
featuresets = [(pos_features(n), g) for (n,g) in tagged_words]
size = int(len(featuresets) * 0.02)
print size
train_set, test_set = featuresets[size:4000], featuresets[:size]

classifier = nltk.DecisionTreeClassifier.train(train_set)
print nltk.classify.accuracy(classifier, test_set)

# print classifier.classify(pos_features('cats'))
print (classifier.pseudocode(depth=4))