# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 10:32:44 2017

@author: cmas
"""

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA

iris = datasets.load_iris()

X=iris.data
y=iris.target
target_names = iris.target_names
pca = PCA(n_components=2) # Number of component to keep
X_r = pca.fit_transform(X)

print('explained variance ratio(first two component): %s'%str(pca.explained_variance_ratio_))

plt.figure()
colors=['navy','turquoise','darkorange']
lw=2

for color,i,target_name in zip(colors,[0,1,2],target_names):
    plt.scatter(X_r[y==i,0],X_r[y==i,1],color=color,alpha=.8,lw=lw,label=target_name)
    plt.legend(loc='best',shadow=False,scatterpoints=1)
    plt.title('PCA of IRIS dataset')
    
plt.show