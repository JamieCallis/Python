from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
from gutenberg.cleanup import strip_headers
import re
import heapq

# ref: https://stackabuse.com/text-summarization-with-nltk-in-python/

class Summarization(object):
    # local variables
    textSummary = ""
    def __init__(self, text):
        # pass in the text, and process the text
        self.original_striped_text = strip_headers(text).strip()
        self.text = strip_headers(text).strip()
        self.sentences = []
        self.word_frequencies = {}
        self.sentence_scores = {}
        self.preprocesstext()
        

    def preprocesstext(self):
        # responsible for handling the calling and building of the text summarization
        self.text = re.sub('[^a-zA-Z.?!]', ' ', self.text)
        self.text = re.sub(r'\s+', ' ', self.text)
        self.text = str(self.text)
        self.tokenizeSentences()
        self.frequencyWeighted()
        self.calculateWorkFrequence()
        self.calculateSentenceScores()
        self.summarise()

    def tokenizeSentences(self):
        # tokenize the sentences
        # Issue we have here is it still takes special characters, which will mess things up later on.
        self.sentences = sent_tokenize(self.text)
        
        
    
    def frequencyWeighted(self):
        stopwords = nltk.corpus.stopwords.words('english')
        
        for word in word_tokenize(self.text):
            if word not in stopwords:
                if word not in self.word_frequencies.keys():
                    self.word_frequencies[word] = 1
                else:
                    self.word_frequencies[word] += 1
       
    def calculateWorkFrequence(self):
        # calculate the frequency of words within the text. 
        maximum_frequency = max(self.word_frequencies.values())
        for word in self.word_frequencies.keys():
           self.word_frequencies[word] = (self.word_frequencies[word]/maximum_frequency)
        

    def calculateSentenceScores(self):
        # calculate the sentence scores.
        for sent in self.sentences:
            for word in word_tokenize(sent.lower()):
                if word in self.word_frequencies.keys():
                    if len(sent.split(' ')) < 50:
                        if sent not in self.sentence_scores.keys():
                            self.sentence_scores[sent] = self.word_frequencies[word]
                        else:
                            self.sentence_scores[sent] += self.word_frequencies[word]
 


    def summarise(self):
        # Look at the top 10 sentences and produce a concatinated summary.
        summary_sentences = heapq.nlargest(10, self.sentence_scores, key=self.sentence_scores.get)
        summary = ' '.join(summary_sentences)
        self.textSummary = summary
        

    def getTextSummarization(self):
        # return the summarization of the text
        return str(self.textSummary)
    
    def getOringalText(self):
        return str(self.original_striped_text)