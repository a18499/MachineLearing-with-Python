# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:34:31 2017

@author: cmas
"""

import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MinMaxScaler
from sklearn import datasets

params=[{'solver':'sgd','learning_rate':'constant','momentum':'0','learning_rate_init':'0.2'},{
        'solver':'sgd','learning_rate':'constant','momentum':'.9','nestervos_momentum':False,'learning_rate_init':'0.2'},
        {'solver':'sgd','learning_rate':'constant','momentum':'.9','nestervos_momentum':True,'learning_rate_init':'0.2'}
