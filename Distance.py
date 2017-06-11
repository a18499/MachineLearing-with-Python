# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 16:08:49 2017

@author: Peter
"""

from numpy import *

#Eiclidean Distance
vector1 = mat([1,2,3])
vector2 = mat([4,5,6])

print (sqrt((vector1-vector2)*((vector1-vector2).T)))

#Manhattan Distance
vector2_1 = mat([1,2,3])
vector2_2 = mat([4,5,6])

print(sum(abs(vector2_1-vector2_2)))

#Chebyshev Distance
vector2_1 = mat([1,2,3])
vector2_2 = mat([4,7,5])
print(abs(vector2_1-vector2_2).max())

#Cosin
vector1 = mat([1,2,3])
vector2 = mat([4,5,6])

cosV12 = dot(vector1,vector2)/(linalg.norm(vector1)*linalg.norm(vector2))

print(cosV12)

#Hamming Distance

matV = mat([[1,1,0,1,0,1,0,0,1],[0,1,1,0,0,0,1,1,1]])

smstr = nonzero(matV[0]-matV[1])

print(shape(smstr[0])[1])