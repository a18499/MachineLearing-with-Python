# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:15:59 2017

@author: cmas
"""

from sklearn.neural_network import MLPClassifier
X=[[0.,0.],[1.,1.]]
y=[0,1]
clf=MLPClassifier(solver="lbfgs",alpha=1e-5, hidden_layer_sizes=(5,2),random_state=1)

print(clf)
clf.fit(X,y)
print(clf.predict([[2.,2.],[-1.,-2]]))
print(clf.predict_proba([[2.,2.],[1.,2.]]))
print([coef.shape for coef in clf.coefs_])
