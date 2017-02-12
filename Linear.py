# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 10:41:25 2017

@author: cmas
"""

from sklearn import linear_model
reg=linear_model.LinearRegression()
reg.fit([[2,1],[3,1],[4,1]],[3,4,5])

print(reg.coef_)

print(reg.intercept_)

reg2=linear_model.LinearRegression()
reg2.fit([[0,0],[1,1],[2,2]],[1,2,3])

print(reg2.coef_)

print(reg2.intercept_)