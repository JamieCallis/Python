'''
    Unicode supports over a million characters. 

    Character is assigned a number, called a code point. 

    In Python, code points are written in the form 
    \uXXXX, where XXXX is the number in four-digit
    hexadecimal form.

    Text in files will be in a particular encoding, so we
    need some mechanism for translating it into Unicode. 

    This is called decoding. 

    If we need to write out to a file, then the process 
    is called encoding.
'''

# -*- coding: <'utf-8'> -*-

# allows us to read encoded files into unicode
import codecs
# f = codecs.open(path, encoding='latin2')

a = u'\u0061'
print a