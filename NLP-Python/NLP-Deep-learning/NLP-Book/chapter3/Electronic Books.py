from __future__ import division
import nltk, re, pprint

# Electronic Books
# http://www.gutenberg.org/catalog/
# contains 25,000 free online books.

# accessing an English translation of 'Crime and Punishment
from urllib import urlopen
url = "http://www.gutenberg.org/files/2554/2554-0.txt"
# gets the string from the text file
raw = urlopen(url).read()
print type(raw)
print len(raw)
print raw[:75]

# The current raw string contains whitespace, and
# other information such as line breaks, and blank lines.

# we want to break the sentence into words and punctuation.

# This is called tokenization.
# we need to decode the string into a readable format for tokenisation
# if we don't we get an encoding error.
tokens = nltk.word_tokenize(raw.decode('utf-8'))
print type(tokens)
print len(tokens)
print tokens[:10]

text = nltk.Text(tokens)
print(text)
print text[1020:1060]
print text.collocations()

# at this point we can not know where text begins, and
# where the text ends.

# manuual inspection
# find the beginning
print raw.find("PART I")
# find the end
print raw.rfind("End of Project Gutenberg's Crime")
# splice to restructure the document
raw = raw[5384:-1]
print raw.find("PART I")
