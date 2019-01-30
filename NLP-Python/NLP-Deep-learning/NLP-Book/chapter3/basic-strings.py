# Basic Operations with Strings

# can use single or double qoutes
monty = 'Monty Python'

# if a string contains a ' we have 
cirus = "Monty Python\'s Flying Circus"

# python provides us with a method to have text on more than
# one line. 

couplet = "Shall I compare thee to a Summer's day?"\
        "Thou are more lovely and more temerate:"

# we can also wrap this in brackets
couplet = ("Shall I compare thee to a Summer's day?"
        "Thou are more lovely and more temerate:")

# we can also access individual characters
print monty[0]

# we can also write loops to print individual character strings
sent = 'colorless green ideas sleep furiously'
for chat in sent:
    print chat,

# we can also count individual characters as well
import nltk
from nltk.corpus import gutenberg
raw = gutenberg.raw('melville-moby_dick.txt')
fdist = nltk.FreqDist(ch.lower() for ch in raw if ch.isalpha())
fdist.keys()
fdist.plot()

# accessing substrings
monty[-12:-7]

# testing a string to see if it contains a given substring
phrase = 'And now for something completely different'

if 'thing' in phrase:
    print 'found "thing"'

# can find the position of a substring using find()
monty.find('Python')

# lists and strings seem simular and are sequence. 
# but we can not join string and lists together. 
# But lists can contain strings inside

'''
    Strings are immutable: you can't change a string once 
    you have created it. However, lists are mutable,
    and their contents can be modified at any time. As
    a result, lists support operations that modify the
    original value rather than producing a new value.
'''