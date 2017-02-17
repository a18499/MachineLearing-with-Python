# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 13:41:44 2017

@author: cmas
"""

import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
rcParams['figure.figsize']=12,10

x=np.array([i*np.pi/180 for i in range(70,300,4)])
np.random.seed(10)
y=np.sin(x)+np.random.normal(0,0.15,len(x))

data = pd.DataFrame(np.column_stack([x,y]),columns=['x','y'])
plt.plot(data['x'],data['y'],'.')

for i in range(2,16):
    colname='x_%d'%i
    data[colname]=data['x']**i
print (data.head())