import nltk

# mapping words to properties using Python Dictionaires

pos = {}

pos['colorless'] = 'ADJ'
pos['ideas'] = 'N'
pos['sleep'] = 'V'
pos['furiously'] = 'ADJ'

print pos

# acessing
print pos['ideas']
print pos['colorless']

for word in sorted(pos):
    print word + ":", pos[word]

# Note that dictionary keys must be immutable types, such as strings and tuples.
# If we try to define a dictionary using a mutable key, we get a TypeError.

# Sepcial kind of dictionary called 'defaultdict' is avaiable.
# Automatically creates an entry for the new key and gives it a default value.
from collections import defaultdict

frequency = defaultdict(int)
frequency['colorless'] = 4
frequency['ideas']

# sets the default type to Noun
pos2 = defaultdict(lambda: 'NOUN')
pos2['colorless'] = 'ADJ'
pos2['blog']
print list(pos2.items())

'''
    Lambda expression

    Specifies no parameters, so we call it using parentheses with no arguments
    thus, the definitions of f and g below are equivalent

    f = lambda: 'NOUN'
    f()
    def g():
        return NOUN
    g()
'''

'''
    Once of the issues with progressing tasks for language is the
    introduction of new vocabuary. 

    We can replace text with low-frequecy words with a special 
    "out of vocabulary" token UNK, using the default dictionary.
'''

alice = nltk.corpus.gutenberg.words('carroll-alice.txt')
vocab = nltk.FreqDist(alice)
v1000 = [word for (word, _) in vocab.most_common(1000)]
mapping = defaultdict(lambda:'UNK')
for v in v1000:
    mapping[v] = v

alice2 = [mapping[v] for v in alice]
print alice[:100]
print len(set(alice2))

# incrementally updating a dictionary and sorting by value

from collections import defaultdict
counts = defaultdict(int)

from nltk.corpus import brown
for (word, tag) in brown.tagged_words(categories='news', tagset='universal'):
    counts[tag] += 1

print counts

sorted(counts)

from operator import itemgetter
print sorted(counts.items(), key=itemgetter(1), reverse=True)
print [t for t, c in sorted(counts.items(), key=itemgetter(1), reverse=True)]

# nltk.index() anagrams
words = nltk.corpus.words.words('en')

anagrams = nltk.Index((''.join(sorted(w)), w) for w in words)
print anagrams['aeilnrt']

# POS tagger
pos = defaultdict(lambda: defaultdict(int))
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
for ((w1, t1), (w2, t2)) in nltk.bigrams(brown_news_tagged):
    pos[(t1, w2)][t2] += 1

print pos[('DET', 'right')]