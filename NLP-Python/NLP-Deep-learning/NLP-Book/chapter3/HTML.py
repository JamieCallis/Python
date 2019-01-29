from __future__ import division
import nltk, re, pprint
from urllib import urlopen
from bs4 import BeautifulSoup

url = "http://news.bbc.co.uk/2/hi/health/2284783.stm"
soup = BeautifulSoup(urlopen(url).read(), 'html.parser')
raw = soup.get_text()
tokens = nltk.word_tokenize(raw)

# nltk provides us with a helper function to take strings
# out of HTML returning raw text.
# This can then be tokenised

tokens = tokens[96:399]
text = nltk.Text(tokens)
text.concordance('gene')
print text

