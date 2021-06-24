# -*- coding: utf-8 -*-
"""
Created on Mon May 10 00:15:07 2021

@author: lopah
"""

from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split


iris = datasets.load_iris()
X=iris.data
y=iris.target

Xtr, Xts, Ytr, Yts = train_test_split(X,y,test_size=0.2 ,random_state = 10)

t1=DecisionTreeClassifier()
t1.fit(Xtr,Ytr)

y_pred = t1.predict(Xts)

t1.score(Xtr,Ytr)
#fully grow tree가 default값임. => score 값이 1이므로!

t1.score(Xts, Yts)
#trainingset 보다는 작지 당연히!

t2=DecisionTreeClassifier(max_depth=3)
t2.fit(Xtr,Ytr)
t2.score(Xtr,Ytr)
#max_depth가 3이므로 fully grow tree 가 아니여서 1이 아님.

y_prob = t1.predict_proba(Xts)
#하나의 클래스 값으로만 분류됨. 0, 0, 1 = class 3

#%% draw tree

from sklearn import tree
import matplotlib.pyplot as plt

tree.plot_tree(t1)

fig=plt.figure(figsize=(10,8))
tree.plot_tree(t1)

fig=plt.figure(dpi=100)
tree.plot_tree(t1)

fig=plt.figure(dpi=200)
tree.plot_tree(t1, feature_names = iris.feature_names, class_names = iris.target_names, filled=True)



#%%Regression Tree

from sklearn.tree import DecisionTreeRegressor

boston = datasets.load_boston()
X=boston.data
y=boston.target

Xtr, Xts, Ytr, Yts = train_test_split(X,y,test_size=0.2 ,random_state = 85)
t3 = DecisionTreeRegressor()
t3.fit(Xtr,Ytr)


#R^2
t3.score(Xts,Yts)
#fully grow tree 가 생김 trainingset이니까 당연!
t3.score(Xtr,Ytr)

#overfitted!!
fig=plt.figure(dpi=100)
tree.plot_tree(t3)

y_pred = t3.predict(Xts)

#overcome overfitted

t4 = DecisionTreeRegressor(max_depth=5, min_samples_split=10,min_samples_leaf = 5)
t4.fit(Xtr,Ytr)

#R^2
t4.score(Xts,Yts)
#depth를 제한했기에 차이가 있음.
t4.score(Xtr,Ytr)

fig=plt.figure(dpi=100)
tree.plot_tree(t4)











































