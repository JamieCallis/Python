from __future__ import division
import nltk, re, pprint
import feedparser
from bs4 import BeautifulSoup

# we have a feed of information 

llog = feedparser.parse("http://languagelog.ldc.upenn.edu/nll/?feed=atom")
print llog['feed']['title']
print len(llog.entries)
# soup = llog

# print nltk.word_tokenize(soup.prettify())
