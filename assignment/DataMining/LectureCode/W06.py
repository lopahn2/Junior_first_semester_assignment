# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 17:20:22 2021

@author: lopah
"""
import numpy as np
from scipy import stats

np.prod([1,2,3,4])
#곱하기

def likelihood(data, dist, args=[], kwds={}):
    return np.prod([dist(x,*args,**kwds) for x in data])
    
def add(a,b):
    return a+b

add(*[3,5]) #값 꺼내기


def norm(x, mu=0, sigma=1):
    return 1/np.sqrt(2*np.pi*sigma**2)*np.exp(-(x-mu)**2/2/sigma**2)

D=[2.61,3.73,2.80,4.29,3.12]

norm(0)
norm(1,mu=1)
norm(1,mu=1,sigma=2)

likelihood(D,norm, [],{'mu':3,'sigma':1})
likelihood(D,norm, kwds={'mu':3,'sigma':1})
likelihood(D, stats.norm.pdf, kwds={'loc':3, 'scale':1})

def bernoulli(x, p):
    return p**x*(1-p)**(1-x)

D=[1,0,1,1,1,0,1,0]

likelihood(D,bernoulli,[0.7])
likelihood(D, stats.bernoulli.pmf,[0.7])


#%%logistic regression model


def logistic(data, beta):
    x=data[:-1]
    y=data[-1]
    p=1/(1+np.exp(-np.dot(x,beta)))
    return p**y*(1-p)**(1-y)

X=[[1,150],[1,160],[1,167],[1,170]]
y=[1,0,1,0]
D=np.c_[X,y]


likelihood(D, logistic, args=[[0.5,0.01]])

from scipy.optimize import minimize

def logLNorm(x, data, sigma=1):
    return sum([-np.log(norm(d,x,sigma))for d in data])

D=[2.61,3.73,2.80,4.29,3.12]

minimize(logLNorm,0,(D,1), method='Nelder-Mead', options={'xatol':1e-8,'disp':True})
#minimize랑 np.mean(D)랑 결과는 같다.
np.mean(D)

#%% classification
import pandas as pd
from sklearn.linear_model import LogisticRegression

height = pd.read_csv('https://drive.google.com/uc?export=download&id=1m0noi5t5StwPdTACZOkP22hKKR6v4vLX')

clf=LogisticRegression()
clf.fit(height[['height']], height['sex'])

clf.coef_
clf.intercept_

y_pred = clf.predict(height[['height']])

np.unique(height['sex'])
#확인 결과 male 에 대한 회귀임

y_prob = clf.predict_proba(height[['height']]) #0 = femail , 1 = male
y_prob.sum(1) # p-female + p-male = 1


#%% multiclassification ~45분

from sklearn import datasets

iris=datasets.load_iris()
X=iris.data
y=iris.target

clf.fit(X,y)
#3개의 클래스가 있기에 3개의 베타셋이 있는 것
clf.coef_ 
clf.intercept_

#clf2=LogisticRegression(mulit_class='ovr')
#clf2.fit(X,y)

#clf2.coef_
#clf2.intercept_

y_pred = clf.predict(X)

y_prob=clf.predict_proba(X)

clf.score(X,y)
#97퍼센트정도로 분류할 수 있음을 의미

















