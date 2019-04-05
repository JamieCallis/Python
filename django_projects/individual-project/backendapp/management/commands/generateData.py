from django.core.management.base import BaseCommand, CommandError
from backendapp.models import BookMetaData
from backendapp.models import BookText

from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers
from gutenberg.query import get_metadata
import json

# as of writting this document 59012 is the last book in the gutenberg dataset. 
def generateBooks(lastBookID):
        firstBookID = 19107
        # look through and grab each book
        while firstBookID <= lastBookID:
            # load and grab the eBook
            try: 
                text = strip_headers(load_etext(firstBookID)).strip()
                gatherMetaData(firstBookID, text)
                firstBookID = firstBookID + 1
            except:
                print("error with book", firstBookID)
                firstBookID = firstBookID + 1

# we need to convert the subject to any bytes array in order for 
# it to be stored in the database.
# The main reason for this is the rest of the information is being stored
# in the database. The other option is to use JSON. 
# But since the text files are gonna be so long we don't want to 
# slow down accessing of the data such we shall store all the information in 
# the SQL database. The other benifit here is it makes accessing the information
# easier using the models.
def gatherMetaData(bookID, text):
    # Meta data types
    ''' taken from - https://github.com/hugovk/gutenberg-metadata
        id
        author
        formaturi - we want to filter or ignore this one. Since we are more interested in the supporting information.
        language
        rights
        subject
        title
        fulltext - we will add this on
    '''
    subjectItems = []

    title, = get_metadata("title", bookID)
    author, = get_metadata("author", bookID)
    language, = get_metadata("language", bookID)
    rights, = get_metadata("rights", bookID)
    subject = get_metadata("subject", bookID)

    for item in subject:
        subjectItems.append(item)
    # the dict needs to be turned into a byte array. 
    # we can do this using the json library.
    # refs: https://stackoverflow.com/questions/19232011/convert-dictionary-to-bytes-and-back-again-python
    SubjectDict = dict(subject=subjectItems)
    SubjectToBytes = json.dumps(SubjectDict)
    # The last step is to turn the binary to a bytes array
    # ref: https://www.w3resource.com/python/python-bytes.php
    binary = bytes(SubjectToBytes, "utf8")
   
    storeInformationIntoDatabase(bookID, text, title, author, language, rights, binary)

def storeInformationIntoDatabase(bookID, text, title, author, language, rights, subjects):
    # method to create and store the files in a txt file, the other options would be to store the information in a database
    
    bookMetaData = BookMetaData(bookID=bookID, title=title, author=author, language=language, rights=rights, subjects=subjects)
    bookText = BookText(bookID=bookMetaData,bookContents=text)
    bookMetaData.save()
    bookText.save()
    print("bookID", bookID, "Has been saved")


class Command(BaseCommand):
    help = 'generate the database data. The meta data and texts for the ebooks'
    
    def add_arguments(self, parser):
        parser.add_argument('my_int_argument', nargs='+', type=int)

    def handle(self, *args, **options):
        # we are know accessing the information correctly
        generateBooks(options['my_int_argument'][0])
    
    
        