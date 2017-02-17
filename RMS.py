# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 22:22:39 2017

@author: a1849
"""

from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
from sklearn.linear_model import LinearRegression
rcParams['figure.figsize'] = 12, 10

#Define input array with angles from 60deg to 300deg converted to radians
x = np.array([i*np.pi/180 for i in range(60,300,4)])
np.random.seed(10)  #Setting seed for reproducability
y = np.sin(x) + np.random.normal(0,0.15,len(x))
data = pd.DataFrame(np.column_stack([x,y]),columns=['x','y'])
plt.plot(data['x'],data['y'],'.')

for i in range(2,2):  #power of 1 is already there
    colname = 'x_%d'%i      #new var will be x_power
    data[colname] = data['x']**i
print (data.head())

def linear_regression(data,power,models_to_plot):
    predictors=['x']
    if power>=2:
        predictors.extend(['x_%d'%i for i in range(2,power+1)])
    print (predictors)    
    
    linreg=LinearRegression(normalize=True)
    linreg.fit(data[predictors],data['y'])
    y_pred=linreg.predict(data[predictors])
    
    if power in models_to_plot:
        plt.subplot(models_to_plot[power])
        plt.tight_layout()
        plt.plot(data['x'],y_pred)
        plt.plot(data['x'],data['y'],".")
        plt.title('Plot for power: %d'%power)
        
    rss = sum((y_pred-data['y'])**2)
    ret=[rss]
    ret.extend([linreg.intercept_])
    ret.extend(linreg.coef_)
    return ret
rms = sqrt(mean_squared_error(y_actual, y_predicted))