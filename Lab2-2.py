# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 11:23:43 2017

@author: cmas
"""

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model

diabetes = datasets.load_diabetes()

diabetes_X=diabetes.data[:,np.newaxis:2]
print("diabetes_X: ",diabetes_X)
diabetes_X_train = diabetes_X[:-20]
print("diabetes_X_train: ",diabetes_X_train)
diabetes_X_test = diabetes_X[-20:]

diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

regr=linear_model.LinearRegression()

regr.fit(diabetes_X_train,diabetes_y_train)

print('Cofficient: \n',regr.coef_)

print("Mean squared error: %.2f"%np.mean((regr.predict(diabetes_X_test)-diabetes_y_test)**2))

print('Variance:%.2f'%regr.score(diabetes_X_test,diabetes_y_test))
"""
plt.scatter(diabetes_X_test,diabetes_y_test,color='black')
plt.plot(diabetes_X_test,regr.predict(diabetes_X_test),color='blue',linewidth=3)

plt.show()
"""