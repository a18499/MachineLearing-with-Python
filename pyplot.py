# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 09:22:38 2017

@author: cmas
"""

import numpy as np
import matplotlib.pyplot as plt
N=50
x=np.random.rand(N)
y=np.random.rand(N)
colors=np.random.rand(N)
area=np.pi*(15*np.random.rand(N))**2
plt.scatter(x,y,s=area,c=colors,alpha=0.5)
           