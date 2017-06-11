# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 23:41:30 2017

@author: user
"""

from numpy import *

featuremat = mat([[88.5,96.8,104.1],[12.54,14.65,57]])

mv1=mean(featuremat[0])
mv2=mean(featuremat[1])

dv1=std(featuremat[0])
dv2=std(featuremat[1])

corref=mean(multiply(featuremat[0]-mv1,featuremat[1]-mv2)/(dv1*dv2))

print(corref)
#use numpy
print(corrcoef(featuremat))