import nltk
from nltk.corpus import brown
from nltk import word_tokenize
import pylab
# setting up data
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')

# The default tagger

tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
# most frequent
print nltk.FreqDist(tags).max()

# tagger that tags everything as NN (Noun)
raw = 'I do not like green eggs and ham, I do not like them Sam I am!'
tokens = word_tokenize(raw)
default_tagger = nltk.DefaultTagger('NN')
print default_tagger.tag(tokens)

# this will perform poorly on a corpus
print default_tagger.evaluate(brown_tagged_sents)

# The regular expression Tagger

# these are processed in order the first one to match applies	
patterns = [
    (r'.*ing$', 'VBG'),               # gerunds
    (r'.*ed$', 'VBD'),                # simple past
    (r'.*es$', 'VBZ'),                # 3rd singular present
    (r'.*ould$', 'MD'),               # modals
    (r'.*\'s$', 'NN$'),               # possessive nouns
    (r'.*s$', 'NNS'),                 # plural nouns
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # cardinal numbers
    (r'.*', 'NN')                     # nouns (default)
]

regexp_tagger = nltk.RegexpTagger(patterns)
print regexp_tagger.tag(brown_sents[3])

print regexp_tagger.evaluate(brown_tagged_sents)

# The Lookup Tagger

# step 1 gather a lot of high-frequency words
fd = nltk.FreqDist(brown.words(categories='news'))
cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
most_freq_words = fd.most_common(100)

# tagging
likely_tags = dict((word, cfd[word].max()) for (word, _) in most_freq_words)
baseline_tagger = nltk.UnigramTagger(model=likely_tags)
print baseline_tagger.evaluate(brown_tagged_sents)

# looking at tags that have been assigned none
sent = brown.sents(categories='news')[3]
baseline_tagger.tag(sent)

# we can use a method called backoff. This is specifying one tagger
# as a parameter to the other
baseline_tagger = nltk.UnigramTagger(model=likely_tags, backoff=nltk.RegexpTagger(patterns))
print baseline_tagger.evaluate(brown_tagged_sents)


# putting it all together
def performance(cfd, wordList):
    lt = dict((word, cfd[word].max()) for word in wordList)
    baseline_tagger = nltk.UnigramTagger(model=lt, backoff=nltk.DefaultTagger('NN'))
    return baseline_tagger.evaluate(brown.tagged_sents(categories='news'))

def display():
    word_freqs = nltk.FreqDist(brown.words(categories='news')).most_common()
    words_by_freq = [w for (w, _) in word_freqs]
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
    sizes = 2 ** pylab.arange(15)
    prefs = [performance(cfd, words_by_freq[:size]) for size in sizes]
    pylab.plot(sizes, prefs, '-bo')
    pylab.title('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()

#display()

# N-Gram Tagging

'''
    Unigram Taggers are based on a simple staistical algorithm,
    for each token, assign the tag that is most likely for that particular
    token.
'''

brown_tagged_sents = brown.tagged_sents(categories='news')
#brown_sents = brown.sents(categories='news')
# unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
# print unigram_tagger.tag(brown_sents[2007])

# print unigram_tagger.evaluate(brown_tagged_sents)

'''
    We train a unigram tagger by specifying tagged sentence data as a
    parameter when we initialize the tagger. The training process
    involves inspecting the tag of each word and storing the most likely
    tag for any word in a dictionary, stored inside the tagger.
'''

# separating the training and testing data
size = int(len(brown_tagged_sents) * 0.9)
print(size)

train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
unigram_tagger = nltk.UnigramTagger(train_sents)
print unigram_tagger.evaluate(test_sents)

'''
    A 1-gram tagger is another term for a unigram tagger: i.e., the
    context used to tag a token is just the text of the token itself.
    2-gram taggers are also called bigram taggers, and 3-gram taggers
    are called trigram taggers.

    The NgramTagger class uses a tagged training corpus to determine which
    part-of-speech tag is most likely for each context.

    In order to combat issues with parse data, we can use multiple
    algorithms to increase coverage.
'''

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents, backoff=t0)
t2 = nltk.BigramTagger(train_sents, backoff=t1)
print t2.evaluate(test_sents)
t3 = nltk.TrigramTagger(train_sents, backoff=t2)
print t3.evaluate(test_sents)


# storing taggers
from pickle import dump
output = open('t2.pkl', 'wb')
dump(t2, output, -1)
output.close()

from pickle import load
input = open('t2.pkl', 'rb')
tagger = load(input)
input.close()

text = """The board's action shows what free enterprise is up against
in our complex maze of regulatory laws ."""
tokens = text.split()
print tagger.tag(tokens)

# performance limitations
cfd = nltk.ConditionalFreqDist(
    ((x[1], y[1], z[0]), z[1])
    for sent in brown_tagged_sents
    for x,y,z in nltk.trigrams(sent)
)

ambiguous_contexts = [c for c in cfd.conditions() if len(cfd[c]) > 1]
print sum(cfd[c].N() for c in ambiguous_contexts) / cfd.N()

# confusion matrix
test_tags = [tag for sent in brown.sents(categories='editorial')
for (word, tag) in t2.tag(sent)]
gold_tags = [tag for (word, tag) in brown.tagged_words(categories='editorial')]
print(nltk.ConfusionMatrix(gold_tags, test_tags))