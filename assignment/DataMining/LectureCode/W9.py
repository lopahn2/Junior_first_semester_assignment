# -*- coding: utf-8 -*-
"""
Created on Sat May  8 20:11:35 2021

@author: lopah
"""

#%% k-NN
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import pairwise_distances

n=20
x=np.random.rand(n)
y=np.random.rand(n)

train = pd.DataFrame(data={'x':x,'y':y})

plt.scatter(x,y)
#random하게 생성된 train set 들의 scatter plot

point=[0.5,0.5] #test sample

d = pairwise_distances(train)

train['dist']= pairwise_distances([point], train, metric = 'euclidean')[0]
#metric 을 menhatan으로 바꾸면 그거 할 수 있어

#find nearest neighbor
sort_train = train.sort_values(by=['dist'])

k=3
r=0.3

print(sort_train.iloc[range(k)])

#fixed range
print(sort_train[sort_train['dist']<r])

#k-nearest neighbor's index
knn_ind=sort_train.iloc[range(k)].index.values
#fixed '''
rnn_ind=sort_train[sort_train['dist']<r].index.values


#k-nearest neighbor
#not_nn_ind=np.setdiff1d(range(n),knn_ind)
#plt.scatter(train.loc[not_nn_ind,'x'], train.loc[not_nn_ind,'y'], c='k') # c='k' = black
#plt.scatter(train.loc[knn_ind,'x'], train.loc[knn_ind,'y'], c='b') # c='b' = blue
#plt.scatter([point[0]],[point[1]], c='r')

#fixed '''
not_nn_ind=np.setdiff1d(range(n),rnn_ind)
plt.scatter(train.loc[not_nn_ind,'x'], train.loc[not_nn_ind,'y'], c='k') # c='k' = black
plt.scatter(train.loc[knn_ind,'x'], train.loc[knn_ind,'y'], c='b') # c='b' = blue
plt.scatter([point[0]],[point[1]], c='r')



#%%sklearn package를 이용한 K-nn

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.model_selection import train_test_split




iris = datasets.load_iris()
X=iris.data
y=iris.target

Xtr, Xts, Ytr, Yts=train_test_split(X,y, test_size=0.2, shuffle=True, random_state = 10)
#test_size => 이만큼은 테스트사이즈로 쓰고, 나머지는 트레인사이즈로 쓰겠다는 뜻
#random_state는 실행시 값을 변하지 않게 해주는 확인자 역할

knn_clf = KNeighborsClassifier(n_neighbors=5)
knn_clf.fit(Xtr,Ytr)

y_pred=knn_clf.predict(Xts)

knn_clf.score(Xts,Yts)

nn=knn_clf.kneighbors()
nn=knn_clf.kneighbors(Xts)
#두번째 배열에서 row는 거리순으로 가까운게 col0 -> col4

y_prop=knn_clf.predict_proba(Xts)



#%% k-NN regression
np.random.seed(10)
Xtr=np.random.rand(200)*10
np.random.seed(10)
Ytr=np.sin(Xtr)*2+np.random.normal(size=200)*0.5

plt.scatter(Xtr,Ytr)

Xts=np.linspace(0,10,50)
y_true=np.sin(Xts)*2

plt.scatter(Xtr,Ytr)
plt.plot(Xts,y_true)

knn_reg=KNeighborsRegressor(n_neighbors=5, weights='distance')
#weight = 'distance' distance에 따라 일정한 가중치를 줍니다.
knn_reg.fit(np.reshape(Xtr,(-1,1)), Ytr)

y_pred = knn_reg.predict(np.reshape(Xts,(-1,1)))

plt.scatter(Xtr,Ytr, c='k')
plt.plot(Xts,y_pred,'r')
#n_neighbor가 커질수록 곡선이 좀더 부드러워짐
#근데 너무 커지면 회귀가 안됨.
#optimal k 를 찾는게 중요
#weight를 주면 k 가 커져도 가까운 놈에게 가중치를 주기 때문에 모양이 고르게 나옴


#%% Fixed-Radius by sklearn

from sklearn.neighbors import RadiusNeighborsClassifier, RadiusNeighborsRegressor


iris = datasets.load_iris()
X=iris.data
y=iris.target

Xtr, Xts, Ytr, Yts=train_test_split(X,y, test_size=0.2, shuffle=True, random_state = 10)

rnn_clf=RadiusNeighborsClassifier(radius=0.5)
rnn_clf.fit(Xtr,Ytr)
rnn_clf.score(Xts,Yts)


y_pred = rnn_clf.predict(Xts)
y_prob=rnn_clf.predict_proba(Xts)

nn=rnn_clf.radius_neighbors()
nn=rnn_clf.radius_neighbors(Xts)

nn[1][0]
nn[1][1]

nn_size=[len(x) for x in nn[1]]


#regression


np.random.seed(10)
Xtr=np.random.rand(200)*10
np.random.seed(20)
Ytr=np.sin(Xtr)*2+np.random.normal(size=200)*0.5
Xts=np.linspace(0,10,50)

rnn_reg = RadiusNeighborsRegressor(radius=1, weights = 'distance')
rnn_reg.fit(np.reshape(Xtr,(-1,1)), Ytr)
y_pred = rnn_reg.predict(np.reshape(Xts,(-1,1)))

plt.scatter(Xtr, Ytr, c='k')
plt.plot(Xts, y_pred,'b')




#%% 맨하튼과 유클리드

iris = datasets.load_iris()
X=iris.data
y=iris.target

Xtr, Xts, Ytr, Yts=train_test_split(X,y, test_size=0.2, shuffle=True, random_state = 10)

#variance 필요 metric_param에

s=np.var(Xtr,axis=0)

knn_clf2 = KNeighborsClassifier(metric='seuclidean', metric_params={'V':s})
knn_clf2.fit(Xtr,Ytr)


cov_mat=np.cov(Xtr.T)
knn_clf3=KNeighborsClassifier(metric='mahalanobis', metric_params={'V':cov_mat})
knn_clf3.fit(Xtr,Ytr)


#%%scale
n=20
x=np.random.rand(n)
y=np.random.rand(n)*10

train = pd.DataFrame(data={'x':x,'y':y})

plt.scatter(x,y)
plt.xlim((0,10))
plt.ylim((0,10))

point=[0.5,5]

k = 3

train['dist'] = pairwise_distances([point],train, metric='euclidean')[0]
sort_train=train.sort_values(by=['dist'])

print(sort_train.iloc[range(k)])

knn_ind=sort_train.iloc[range(k)].index.values
not_nn_ind=np.setdiff1d(range(n),knn_ind)


not_nn_ind=np.setdiff1d(range(n),knn_ind)
plt.scatter(train.loc[not_nn_ind,'x'], train.loc[not_nn_ind,'y'], c='k') # c='k' = black
plt.scatter(train.loc[knn_ind,'x'], train.loc[knn_ind,'y'], c='b') # c='b' = blue
plt.scatter([point[0]],[point[1]], c='r')

plt.xlim((0,10))
plt.ylim((0,10))


#%% normalization

from sklearn.preprocessing import scale

new_train = scale(train[['x','y']])

new_train.mean(0)
new_train.var(0)


#min-max normalization
new_train=(train[['x','y']]-train[['x','y']].min())/(train[['x','y']].max()-train[['x','y']].min())

new_train['dist']=pairwise_distances([[0.5,0.5]],new_train, metric='euclidean')[0]

sort_new_train = new_train.sort_values(by=['dist'])
print(sort_new_train.iloc[range(k)])

#scaling에 대한 정규화

























