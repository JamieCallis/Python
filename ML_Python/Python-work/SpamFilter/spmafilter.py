# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 21:41:53 2017
Used as a guide:
     https://github.com/udacity/machine-learning/blob/master/projects/practice_projects/naive_bayes_tutorial/Naive_Bayes_tutorial.ipynb
@author: jamie
"""

"""

Bag of Words function, starts by making all characters lower case, then filters out he punctuation. 
The next step is to process the strings, into single words by spliting the words up. 
Lastly the documents are procssed with a counter to see the frequency of the words. 

lower_case_documents= []
for i in documents:
    lower_case_documents.append(i.lower())


sans_punctuation_documents = []
import string
for i in lower_case_documents:
    sans_punctuation_documents.append(i.translate(str.maketrans('', '', string.punctuation)))


preprocessed_documents = []
for i in sans_punctuation_documents:
    preprocessed_documents.append(i.split(' '))


frequency_lists = []
import pprint
from collections import Counter
for i in preprocessed_documents:
    frequency_counts = Counter(i)
    frequency_lists.append(frequency_counts)
pprint.pprint(frequency_lists)

***BIG BAG OF WORKS using SKLERAN ***

documents = ['Hello, how are you!', 
            'Win money, win from home.',
            'Call me now.',
            'Hello, Call hello you tomorrow?']


from sklearn.feature_extraction.text import CountVectorizer
count_vector = CountVectorizer()

count_vector.fit(documents)
count_vector.get_feature_names()

doc_array = count_vector.transform(documents).toarray()


frequency_matrix = pd.DataFrame(doc_array, columns = count_vector.get_feature_names())

# Bayes Theorem implementation from scratch

# P (D)
p_diabetes = 0.01

# P(~D)
p_no_diabetes = 0.99

# Sensitivity or P(Ps|D)
p_pos_diabetes = 0.9

# Specificity or P(Neg|~D)
p_neg_no_diabetes = 0.9

# P(Pos)
p_pos = (p_diabetes * p_pos_diabetes) + (p_no_diabetes * (1 - p_neg_no_diabetes))
print('The probability of getting a positive test result P(Pos) is: {}',format(p_pos))

# P(D|Pos)
p_diabetes_pos = (p_diabetes * p_pos_diabetes) / p_pos
                 
print('Probability of an individual having diabetes, given that that individual got a positive test result is:\
',format(p_diabetes_pos))

# P(~D|Pos)
p_pos_no_diabetes = 0.1

# P(~D|Pos)
p_no_diabetes_pos = (p_no_diabetes * p_pos_no_diabetes) / p_pos
                    
print ('Probability of an individual not having diabetes, given that that individual got a positive test result is:'\
,p_no_diabetes_pos)




"""

import pandas as pd
#Dataset from - https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection
df = pd.read_table('SMSSpamCollection', 
                   sep='\t', 
                   header = None,
                   names=['label', 'sms_message'])


#output printing out first 5 colums 
df['label'] = df.label.map({'ham':0,'spam':1})
print(df.shape)

df.head() #returns (rows,colums)


from sklearn.cross_validation import train_test_split
"""

    X_train is our training data for the 'sms_message' column.
    y_train is our training data for the 'label' column
    X_test is our testing data for the 'sms_message' column.
    y_test is our testing data for the 'label' column Print out the number 
    of rows we have in each our training and testing data.
    
"""
X_train, X_test, y_train, y_test = train_test_split(df['sms_message'],
                                                    df['label'],
                                                    random_state=1)

from sklearn.feature_extraction.text import CountVectorizer

# Instantiate the CountVectorizer method
count_vector = CountVectorizer()

# Fit the training data and then return the matrix
training_data = count_vector.fit_transform(X_train)

# Transform testing data and return the matrix. Note we are not fitting the 
# testing data into the CountVectorizer()

testing_data = count_vector.transform(X_test)

from sklearn.naive_bayes import MultinomialNB
naive_bayes = MultinomialNB()
naive_bayes.fit(training_data, y_train)
predictions = naive_bayes.predict(testing_data)


from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
print('Accuracy score: ', format(accuracy_score(y_test, predictions)))
print('Precision score: ', format(precision_score(y_test, predictions)))
print('Recall score: ', format(recall_score(y_test, predictions)))
print('F1 score: ', format(f1_score(y_test, predictions)))






