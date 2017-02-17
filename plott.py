# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 23:42:44 2017

@author: a1849
"""

import numpy as np
import matplotlib.pyplot as plt
x = np.array([2,3,1,0])
for i in range(2,16):
    print(i)
    np.append(x,i)
    
print(x)
y=np.sin(x)
plt.plot(y,x)