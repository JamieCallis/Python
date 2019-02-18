# Gender identification program using text classification
import nltk
import random
import re
from nltk.corpus import names
from nltk.classify import apply_features


'''
    Names ending in a, e, and i are likely to be female,
    while names ending in k, o, r, s and t are likely to be male.
'''

# feature extractor
def gender_features(word):
    return {'suffix1': word[-1:],
            'suffix2': word[-2:]}

# preapring data set
labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
[(name, 'female') for name in names.words('female.txt')])

random.shuffle(labeled_names)

# extracting process building test / train datasets
featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
train_names = labeled_names[1500:]
devtest_names = labeled_names[500:1500]
test_names = labeled_names[:500]

'''
    When working with large corpora, constructing a single list can 
    take up a large amount of memory.

    We can use nltk.classify.apply_features

    Returns an object that acts like a list but does not store all the 
    feature sets in memory.

    train_set = apply_features(gender_features, labeled_names[500:])
    test_set = apply_features(gender_features, labeled_names[:500])
'''

train_set = [(gender_features(n), gender) for (n, gender) in train_names]
devtest_set = [(gender_features(n), gender) for (n,gender) in devtest_names]
test_set = [(gender_features(n), gender) for (n,gender) in test_names]
classifer = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifer, devtest_set))

#print classifer.show_most_informative_features(5)

errors = []

for (name, tag) in devtest_names:
    guess = classifer.classify(gender_features(name))
    if guess != tag:
        errors.append((tag, guess, name))

for(tag, guess, name) in sorted(errors):
    print('correct={:<8} guess={:<8s} name={:<30}'.format(tag, guess, name))

'''
    The error process would be continued with analysis and when a model
    is ready. It should be tested againsted the test_set.
'''

