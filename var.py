# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 17:01:09 2017

@author: tseyunghuang
"""

import tensorflow as tf

var = tf.Variable(0,name ='counters')

one = tf.constant(1)

new_value = tf.add(var,one)
update = tf.assign(var, new_value)

# tf.initialize_all_variables() no long valid from
# 2017-03-02 if using tensorflow >= 0.12
if int((tf.__version__).split('.')[1]) < 12 and int((tf.__version__).split('.')[0]) < 1:
    init = tf.initialize_all_variables()
else:
    init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(var))