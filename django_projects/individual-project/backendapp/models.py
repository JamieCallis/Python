from django.db import models


# Create your models here.
class trainingData(models.Model):
    pass

    # todo : create a model for training data that can be used to train
    # the Spacy model.

class BookMetaData(models.Model):
    # We want to pass the information when creating grabbing the information to store the information we need in our database. 
    # Once we can then confirm the information is inside the database we can build model methods to access the required information.
    bookID = models.BigIntegerField(primary_key=True)
    title = models.CharField('Book Title', max_length=500)
    author = models.CharField('Book Author', max_length=500)
    language = models.CharField('Book language', max_length=10)
    rights = models.CharField('Book Rights', max_length=500)
    subjects = models.BinaryField(blank=bool)

    def __str__(self):
        return self.title

class BookText(models.Model):
    # by adding in a foreign key whenever a book is deleted the text will
    # be deleted along with it.
    # primary key will automatically be generated when migrate occurs.
    # Since every table has to have a unique ID identifier. 
    id = models.AutoField(primary_key=True)
    bookID = models.ForeignKey(BookMetaData, on_delete=models.CASCADE)
    bookContents = models.TextField()