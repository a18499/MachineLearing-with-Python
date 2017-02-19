# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 11:15:44 2017

@author: cmas
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

np.random.seed(0)
X=np.r_[np.random.randn(20,2)-[2,2],np.random.randn(20,2)+[0,0]]
Y=[0]*20+[1]*20
  
clf=svm.SVC(kernel='linear',C=0.01)
clf.fit(X,Y)


w=clf.coef_[0]
a=-w[0]/w[1]
xx=np.linspace(-5,5)
yy=a*xx-(clf.intercept_[0]/w[1])


b=clf.support_vectors_[0]
yy_down=a*xx+(b[1]-a*b[0])
b=clf.support_vectors_[-1]
yy_up=a*xx+(b[1]- a*b[0])

plt.plot(xx,yy,'k-')
plt.plot(xx,yy_down,'k--')
plt.plot(xx,yy_up,'k--')

plt.scatter(clf.support_vectors_[:,0],clf.support_vectors_[:,1],s=80,facecolors='none')

plt.scatter(X[:,0],X[:,1],c=Y,cmap=plt.cm.Paired)

plt.axis('tight')
plt.show()
A4=range(10)
A4=[i for i in range(10) if i in [1,3,2,5,4]]
print(A4)