# -*- coding: utf-8 -*-
"""
Created on Mon May 24 03:26:30 2021

@author: lopah
"""

from sklearn import datasets
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

X,y = datasets.make_regression(n_samples=200, n_features=10, n_informative=3, effective_rank=2)

pca = PCA()
pca.fit(X)

comp = pca.components_
#each row is a principle component. not col. Wt와 같음.
pca.mean_
X.mean(0)

#mean = 0 으로 setting
X0 = X - pca.mean_

#길이는 프린시플 컴포넌트와 길이가 같음.
#eigen value들의 값이 저장.
pca.explained_variance_

exp_var = pca.explained_variance_

#covariance matrix
cov_mat=np.cov(X0.T)


#이하 두개는 거의 같다.
np.diag(cov_mat).sum()
exp_var.sum()



t = np.dot(X0,comp[0])
np.var(t)
exp_var[0]


pca.explained_variance_ratio_

sum(pca.explained_variance_ratio_) #== 1
exp_var/exp_var.sum()


cum_exp_var_ratio = np.cumsum(pca.explained_variance_ratio_)

plt.plot(range(1,11), cum_exp_var_ratio)



T=pca.transform(X)
#T.shape() == X.shape()

pca=PCA(n_components=2)
pca.fit(X)
T=pca.transform(X)
#T.shape() !== X.shape()


pca = PCA()
pca.fit(X)

X0 = X - pca.mean_
comp = pca.components_

T2 = np.matmul(X0,comp[:2].T)
T=pca.transform(X)



plt.scatter(T2[:,0], T2[:,1])



#%%Iris dataset

iris = datasets.load_iris()
X=iris.data
y=iris.target

pca = PCA(n_components=2)
pca.fit(X)

T= pca.transform(X)
plt.scatter(X[:,0],X[:,1],c=y)
plt.scatter(T[:,0],T[:,1],c=y)

pca.explained_variance_

#%% Image data set


from scipy.io import loadmat
import os

datapath = r'C:/Users/lopah/Desktop/SeoulTEch/DataMining'
imgs = loadmat(os.path.join(datapath,'Yale_64x64.mat'))

image = imgs['fea']
label=imgs['gnd'].flatten()

plt.imshow(np.reshape(image[0],(64, 64)).T, cmap=plt.cm.gray)

pca=PCA()

pca.fit(image)
comps = pca.components_
mean_vec=pca.mean_

plt.imshow(np.reshape(mean_vec,(64, 64)).T, cmap=plt.cm.gray)
cb=plt.imshow(np.reshape(comps[0],(64, 64)).T, cmap=plt.cm.gray)
plt.colorbar()


all_ind = range(len(label))
val_ind = np.array([np.random.choice(np.where(label==i)[0],1) for i in np.unique(label)]).flatten()
train_ind = np.setdiffld(all_ind,val_ind)

Xtrn = image[train_ind]
Ytrn = label[train_ind]
Xval = image[val_ind]
Yval = label[val_ind]

pca = PCA()
pca.fit(Xtrn)

Xtrn_T = pca.transform(Xtrn)
Xval_T = pca.transform(Xval)

from sklearn.linear_model import LogisticRegression

clf = LogisticRegression()

result = []
for npc in range(1, comp.shape[0]+1):
    clf.fit(Xtrn_T[:,:npc], Ytrn)
    result.append(clf.score(Xval_T[:,:npc],Yval))

clf.fit(Xtrn, Ytrn)
acc_orig = clf.score(Xval, Yval)

plt.plot(range(1,comp.shape[0]+1), result)
plt.hlines(acc_orig,1,comp.shape[0]+1, linestyle='--')





































