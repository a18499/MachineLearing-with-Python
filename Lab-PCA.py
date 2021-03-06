# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 11:34:43 2017

@author: cmas
"""

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import proj3d

np.random.seed(0)

mu_vec1=np.array([0,0,0])
cov_mat1=np.array([[1,0,0],[0,1,0],[0,0,1]])
class1_sample = np.random.multivariate_normal(mu_vec1,cov_mat1,20).T
assert class1_sample.shape==(3,20),"The matrix has not the dimensions 3x20"

mu_vec2=np.array([1,1,1])
cov_mat2=np.array([[1,0,0],[0,1,0],[0,0,1]])
class2_sample = np.random.multivariate_normal(mu_vec2,cov_mat2,20).T
assert class2_sample.shape==(3,20),"The matrix has not the dimensions 3x20"

fig=plt.figure(figsize=(8,8))
ax=fig.add_subplot(111,projection='3d')
plt.rcParams['legend.fontsize']=10
ax.plot(class1_sample[0,:],class1_sample[2,:],'o',markersize=8,color='blue',alpha=0.5,label='class1')
ax.plot(class2_sample[0,:],class2_sample[2,:],"^",markersize=8,alpha=0.5,color='red',label='class2')

plt.title('Sample for class1 and class2')
ax.legend(loc='upper right')
                             
#Draw line
all_samples= np.concatenate((class1_sample,class2_sample),axis=1)
assert all_samples.shape == (3,40),"The matrix has not thedimensoins 3x40"

mean_x = np.mean(all_samples[0,:])
mean_y = np.mean(all_samples[1,:])
mean_z = np.mean(all_samples[2,:])

mean_vector = np.array([mean_x],[mean_y],[mean_z])

print('Mean Vector:\n',mean_vector)

scatter_matrix()= np.zeros((3,3))
for i in range(all_samples.shape[1]):
    scatter_matrix+=(all_samples[:,i].reshape(3,1)-mean_vector).dot((all_sample[:,i].reshape(3,1)-mean_vector).T)
print('Scatter Matrix:\n', cov_mat)

cov_mat = np.cov([all_samples[0,:],all_samples[1,:],all_samples[2,:]])


eig_val_sc, eig_vec_sc = np.linalg.eig(scatter_matrix)

eig_val_cov, eig_vec_cov = np.linalg.eig(cov_mat)

for i in range(len(eig_val_sc)):
    eigvec_sc=eig_vec_sc[:,i].reshape(1,3).T
    eigvec
    
