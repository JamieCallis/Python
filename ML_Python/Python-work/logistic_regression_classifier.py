# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:09:18 2017

@author: jamie
"""

"""
    * Logistic Regression classifer *
"""

import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

def visualize_classifier(classifier, x , y):
    """
        Define the minimum and maximum values for x and y
        that will be used in the mesh grid
    """
    min_x, max_x = x[:, 0].min() - 1.0, x[:, 0].max() + 1.0
    min_y, max_y = x[:, 1].min() - 1.0, x[:, 1].max() + 1.0

    # Define the step size to use in politting the mesh grid
    mesh_step_size = 0.01
    
    # Define the mesh grid of X and Y values
    x_vals, y_vals = np.meshgrid(np.arange(min_x, max_x, mesh_step_size),
                                 np.arange(min_y, max_y, mesh_step_size))
    
    # Run the classifier on the mesh grid
    output = classifier.predict(np.c_[x_vals.ravel(), y_vals.ravel()])
    
    output = output.reshape(x_vals.shape)
    
    # Create a plot
    plt.figure()
    
    # Choose a color scheme for the plot
    plt.pcolormesh (x_vals, y_vals, output, cmap=plt.cm.gray)
    
    #overlay the training points on the plot
    plt.scatter(x[:, 0], x[:, 1], c=y, s=75, edgecolor='black', linewidth=1, cmap=plt.cm.Paired)
    
    # Specify the boundaries of the polt
    plt.xlim(x_vals.min(), x_vals.max())
    plt.ylim(y_vals.min(), y_vals.max())
    
    # Specify the ticks on the x and y axes
    plt.xticks((np.arange(int(x[:, 0].min() - 1), int(x[:, 0].max() + 1), 1.0)))
    plt.xticks((np.arange(int(x[:, 1].min() - 1), int(x[:, 1].max() + 1), 1.0)))
    
    plt.show()

# Define sample input data
X = np.array([[3.1, 7.2], [4, 6.7], [2.9, 8], [5.1, 4.5], [6, 5], [5.6, 5],
[3.3,0.4], [2.9, 0.9], [2.8, 1], [0.5, 3.4], [1, 4], [0.6, 4.9]])
y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3])

# Create the logistic regression classifer
classifier = linear_model.LogisticRegression(solver='liblinear', C=100)

# Train the classifer
classifier.fit(X, y)

# Visualize the performance of the classifier by looking at the boundaries of the classes:
visualize_classifier(classifier, X, y)

