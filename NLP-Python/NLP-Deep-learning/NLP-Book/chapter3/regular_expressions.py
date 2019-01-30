# -*- coding: utf-8 -*-

import re
import nltk

#wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]

# Using basic metacharacters


# using the re.search(p, s)

# finding words ending in ed. 
# $ matches the end of a string
#[w for w in wordlist if re.search('ed$', w)]

# The . wildcard symbol matches any single chracter
# ^ matches the start of a string
#[w for w in wordlist if re.search('^..j..t..$', w)]

# the ? symbol specifies that the previous character is optional

#sum (1 for w in wordlist if re.search('^e-?mail$', w))

# The T9 system is used for entering text on mobile phones

'''
    1       2[ABC]  3[DEF]
    4[GHI]  5[JKL]  6[MNO]
    7[PQRS] 6[TUV]  9[WXYZ]
'''

# Two or more words that are entered with the same sequence
# of keystrokes are known as 'textonyms'
# + means "one or more instances of the preceding item"
# print [w for w in wordlist if re.search('^[ghi][mmo][jlk][def]$', w)]
# print [w for w in wordlist if re.search('^[ghijklmno]+$', w)]
# print [w for w in wordlist if re.search('^[a-fj-o]+$', w)]

# chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))
# print [w for w in chat_words if re.search('^m+i+n+e+$', w)]

# print [w for w in chat_words if re.search('^[ha]+$', w)]

# * symbol means "zero or more instances of the prceding item."
# print [w for w in chat_words if re.search('^m*i*n*e*$', w)]
# Note that the + and * symbols are sometimes referred to
# as Kleene closures, or simply closures

# The ^ operator has another function when it appears as the
# first character inside square brackets.

# print [w for w in chat_words if re.search('^[^aeiouAEIOU]+$', w)]

# other symbols that can be used is \, {}, (), |

# \ deprives the following chracter of it's special pwoers
# turning the specific characters into it's literal meaning.

# The braced exppresions like {3,5} specify the number of 
# repeats of the previous item.

# The pipe '|' chracter indicates a choice between the
# material on it's left and it's right.

# The Parentheses () indicate the scope of an operator,
# and they can be used together with the pipe (or disjunction)
# symbol. 

# wsj = sorted(set(nltk.corpus.treebank.words()))

# print [w for w in wsj if re.search('^[0.9]+\.[0-9]+$', w)]

# print [w for w in wsj if re.search('^[0-9]{4}$', w)]

# print [w for w in wsj if re.search('^[A-Z]+\$$', w)]

# print [w for w in wsj if re.search('^[a-z]{5,}-[a-z]{2,3}-[a-z]{,6}$', w)]

# print [w for w in wsj if re.search('(ed|ing)$', w)]

# extracting word peices

'''
 The re.findall() method finds all (non-overlapping) matches
 of the given regular expression.
'''

# word = 'supercalifragilisticexpildocious'
# print re.findall(r'[aeiou]', word)

# print len(re.findall(r'[aeiou]', word))

'''
    Look for all sequences of two or more vowels in some text,
    and determine their relative frequency.
'''

# wsj = sorted(set(nltk.corpus.treebank.words()))
# fd = nltk.FreqDist(vs for word in wsj for vs in re.findall(r'[aeiou]{2,}', word))
# print fd.items()

# regexp = r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'

# def compress(word):
#     pieces = re.findall(regexp, word)
#     return ''.join(pieces)

# english_udhr = nltk.corpus.udhr.words('English-Latin1')
# print nltk.tokenwrap(compress(w) for w in english_udhr[:75])

# rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
# cvs = [cv for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]', w)]
# cfd = nltk.ConditionalFreqDist(cvs)
# cfd.tabulate()

# cv_word_pairs = [(cv, w) for w in rotokas_words
#                         for cv in re.findall(r'[ptksvr][aeiou]', w)]
# cv_index = nltk.Index(cv_word_pairs)
# print cv_index['su']
# print cv_index['po']


# finding word stems 

'''
    For some programming tasks we want to ignore word endings
    and just deail with word stems.
'''

# def stem(word):
#     for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
#         if word.endswith(suffix):
#             return word[:-len(suffix)]
#         return word

# Build up a disjunction of all the suffixes.
# We need to enclose it in () in order to limit
# the scope of the disjunction.
#print re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing')

# If we want to use the () to specify the scope of the
# disjunction but not to select the material to be output
# we have to add ?:
#print re.findall(r'^.*(?:ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processes')

# We can also split the word into stem and suffix
#print re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processes')

def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    stem, suffic = re.findall(regexp, word)[0]
    return stem

raw = """DENNIS: Listen, strange women lying in pond distributing swords
is no basis for a system of government. Supreme executive power derives from a
mandate from the masses, not from some farcial aquatic ceremony."""

tokens = nltk.word_tokenize(raw)
print [stem(t) for t in tokens]

# page 121 - searching tokenized Text







