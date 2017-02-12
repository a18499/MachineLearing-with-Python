# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 15:28:32 2017

@author: cmas
"""
import math
import sys
var= 1
var2 =2
va3 = var+var2
print (va3)
print("Test ")
print(22,33,44,55,sep=":")

print("PI=%.3f"%math.pi)
help(sys)
count = 100
print(count)

a=['sqpm','eggs',100,1234]
print(a)
print(a[:-1])
print(a[1:-1])

print(a[:3]+['bacon',2*2])
print(a[:])

q=[2,3]
p=[1,q,3]
print(p)
print(p[1][1])
p[1].append("Test")

print(p)
print(q)

#LIST
myList=[1,2,3,4]
myList.insert(1,2)
print(myList)
#ZIP
aa="12345"
ab=(1,2,3,4,5)
ac=[1,2,3,4,5]
ad=zip(aa,ab,ac)
for i in ad:
    print(i)
#Assignment
x=3
y=x
y=4
print(x)

#Tuple
tuple = ('a,b,c,d')

print(tuple)

#Flow Control
var1=100
if var1:
    print("1- Got true expression value")
    print(var1)
else:
    print(var1)    
#For
fibonacci = [0,1,1,2,3,5,8,13]
print(len(fibonacci))
for i in range(len(fibonacci)):
    print(i,fibonacci[i])

#Pass by value 
def changeMe(myLists):
	myLists.append("Test")
	print(myLists, sep=' ', end='\n')

changeMe(myList)
print(myList)
#Pass by reference



import numpy as np

x= np.array([2,3,1,0], dtype=None, copy=True, order=None, subok=False, ndmin=0)
x= np.array([2,3,4,5], dtype=None, copy=True, order=None, subok=False, ndmin=0)
print(x, sep=' ', end='\n', file=sys.stdout)
print(x.shape)

xp=np.arange(10)
xp[2:5]
print(xp[2:5])
print(xp[1:7])
print(x[1:7:2])
xp=np.arange(100)
print(xp.shape)
import matplotlib.pyplot as plt

cc=np.arange(0,5,0.1)



