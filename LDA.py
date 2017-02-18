# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 13:28:05 2017

@author: cmas
"""

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

iris = datasets.load_iris()

X=iris.data
y=iris.target
target_name = iris.target_names
lda=LinearDiscriminantAnalysis(n_components=2)
X_r=lda.fit_transform(X,y)

colors=['navy','turquoise','darkorange']

for color, i,target_name in zip(colors,[0,1,2],target_names):
    plt.scatter(X_r[y==i,0],X_r[y==i,1],color=color,alpha=.8, lw=lw,label=target_name)
plt.legend(loc='best',shadow=False,scatterpoints=1)
plt.title('PCA of IRIS dataset')

plt.show()