# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 11:05:01 2017

@author: tseyunghuang
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('TestAll.csv')
Logging_Data = dataset.iloc[:, 1:14].values
Label = dataset.iloc[:, 14].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(Logging_Data, Label, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
docker_train = sc.fit_transform(X_train)
docker_test = sc.transform(X_test)


def add_layer(inputs, in_size, out_size,n_layer, activation_function=None):
     layer_name = 'layer%s' % n_layer
     with tf.name_scope(layer_name):
        with tf.name_scope('Weights'):
            Weights = tf.Variable(tf.random_normal([in_size, out_size]))
        with tf.name_scope('Biases'):    
            biases = tf.Variable(tf.zeros([1, out_size]) + 0.2)
        with tf.name_scope('Formula'):
            Wx_plus_b = tf.matmul(inputs, Weights) + biases
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs

def compute_accuracy(v_xs, v_ys):
    global prediction
    y_pre = sess.run(prediction, feed_dict={xs: v_xs})
    
    correct_prediction = tf.equal(y_pre, v_ys)
    floats=tf.cast(correct_prediction, tf.float32)
    print("correct_prediction:"+str(floats))
    with tf.name_scope('acc'):
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        tf.summary.scalar('acc', accuracy)
    result = sess.run(accuracy, feed_dict={xs: v_xs, ys: v_ys})
    return result

def next_batch(num, data, labels):
    '''
    Return a total of `num` random samples and labels. 
    '''
    idx = np.arange(0 , len(data))
    np.random.shuffle(idx)
    idx = idx[:num]
    data_shuffle = [data[ i] for i in idx]
    labels_shuffle = [labels[ i] for i in idx]

    return np.asarray(data_shuffle), np.asarray(labels_shuffle)
# define placeholder for inputs to network
xs = tf.placeholder(tf.float32, [None, 13]) # 28x28
ys = tf.placeholder(tf.float32, [None,])

# add hidden layer
l1 = add_layer(xs, 13, 6,n_layer=1, activation_function=tf.nn.relu)

# add hidden layer
l2 = add_layer(l1, 6, 6,n_layer=1, activation_function=tf.nn.relu)

# add output layer
prediction = add_layer(l2, 6, 1,n_layer=1,  activation_function=tf.nn.sigmoid)

# the error between prediction and real data

cross_entropy = tf.reduce_mean(-tf.reduce_sum(ys * tf.log(prediction),
                                              reduction_indices=[1]))       # loss
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

sess = tf.Session()

merged = tf.summary.merge_all()

writer = tf.summary.FileWriter("F:\\tensorboardLog\\", sess.graph)

# important step
# tf.initialize_all_variables() no long valid from
# 2017-03-02 if using tensorflow >= 0.12
if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
    init = tf.initialize_all_variables()
else:
    init = tf.global_variables_initializer()




# Later, launch the model, initialize the variables, do some work, save the
# variables to disk.
with tf.Session() as sess:
  sess.run(init)
  for i in range(1000):
    batch_xs, batch_ys = next_batch(100,docker_train,y_train)
   #dataset.train.n
    sess.run(train_step, feed_dict={xs: batch_xs, ys: batch_ys})
    if i % 50 == 0:
       result = sess.run(merged,feed_dict={xs: docker_train, ys: y_train})
       writer.add_summary(result, i)
  # Save the variables to disk.



