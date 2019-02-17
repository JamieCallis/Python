import nltk

#text = nltk.word_tokenize("And now for something completely different")
#print nltk.pos_tag(text)

''' Result - returns a list of truples (key, value pairs)
    [('And', 'CC'), ('now', 'RB'), ('for', 'IN'), 
    ('something', 'NN'), ('completely', 'RB'), 
    ('different', 'JJ')]    
'''

# nltk provides documentation for each tag, which can be queried
# using nltk.help.upenn_tagset('tag')

# the brown corpus is a collection of words that are catagoried.
#text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
# print text.similar('women')
# print text.similar('bought')
# print text.similar('over')
# print text.similar('the')

# representing tagged tokens
tagged_token = nltk.tag.str2tuple('fly/NN')
print tagged_token
print tagged_token[0]
print tagged_token[1]

# we can take this a step further by applying it to sentences
# this can be used to build datasets for testing / training
sent = '''The/AT grand/JJ jury/NN commented/VBD on/IN a/AT number/NN of/IN
other/AP topics/NNS ,/, AMONG/IN them/PPO the/AT Atlanta/NP and/CC
Fulton/NP-tl County/NN-tl purchasing/VBG departments/NNS which/WDT it/PPS
said/VBD ``/`` ARE/BER well/QL operated/VBN and/CC follow/VB generally/RB
accepted/VBN practices/NNS which/WDT inure/VB to/IN the/AT best/JJT
interest/NN of/IN both/ABX governments/NNS ''/'' ./.'''

print [nltk.tag.str2tuple(t) for t in sent.split()]

# Reading Tagged Corpora

print nltk.corpus.brown.tagged_words()
#print nltk.corpus.brown.tagged_words(simplify_tags=True)

# whenever a corpus contains tagged text, the NLTK corpus interface
# will have a tagged_words() method.

# finding the most common tag in a corpus
from nltk.corpus import brown
brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
print tag_fd.keys()

#tag_fd.plot(cumulative=True)

# bigrams = [
#     (('The', 'DET'), ('Fulton', 'NP')),
#     (('Fulton', 'NP'), ('County', 'N'))
# ]

# word_tag_pairs = nltk.bigrams(bigrams)
# print list(nltk.FreqDist(a[1] for (a,b) in word_tag_pairs if b[1] == 'N'))

# wsj = nltk.corpus.treebank.tagged_words()
# word_tag_fd = nltk.FreqDist(wsj)
# print [word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('V')]

# items being counted in the frequency distribution are word-tag pairs.

# cfd1 = nltk.ConditionalFreqDist(wsj)
# print cfd1['yield'].keys()
# print cfd1['cut'].keys()

# cfd2 = nltk.ConditionalFreqDist((tag, word) for (word, tag) in wsj)
# print cfd2['VN'].keys()

# finding the most frequent noun tags for each noun part-of-speech type
def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].keys()[:5]) for tag in cfd.conditions())

tagdict = findtags('NN', nltk.corpus.brown.tagged_words(categories='news'))
for tag in sorted(tagdict):
    print tag, tagdict[tag]

# Exploring Tagged Corpora
brown_learned_text = brown.words(categories='learned')
print sorted(set(b for (a,b) in nltk.bigrams(brown_learned_text) if a == 'often'))

#However it's probably more isntructive to use tagged_words()

brown_lrnd_tagged = brown.tagged_words(categories='learned', tagset='universal')
tag = [b[1] for (a,b) in nltk.bigrams(brown_lrnd_tagged) if a[0] =='often']
fd = nltk.FreqDist(tag)
fd.tabulate()

# finding words involving particular sequences of tags and words e.g. <verb> to <verb>

def process(sentence):
    for(w1,t1), (w2,t2), (w3,t3) in nltk.trigrams(sentence):
        if (t1.startswith('V') and t2 == 'TO' and t3.startswith('V')):
            print(w1, w2, w3)

for tagged_sent in brown.tagged_sents():
    process(tagged_sent)

brown_news_tagged = brown.tagged_words(categories='news', tagset='universal')
data = nltk.ConditionalFreqDist((word.lower(), tag) for (word, tag) in brown_news_tagged)

for word in sorted(data.conditions()):
    if len(data[word]) > 3:
        tags = [tag for (tag, _) in data[word].most_common()]
        print(word, ' '.join(tags))

nltk.app.concordance()




