# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 23:11:02 2021

@author: lopah
"""

from sklearn.linear_model import LinearRegression
from sklearn import datasets

diabets=datasets.load_diabetes()
X=diabets.data
y=diabets.target

reg=LinearRegression()
reg.fit(X,y)

y_pred = reg.predict(X)

error = y - y_pred

import matplotlib.pyplot as plt

plt.hist(error, bins=20)

import numpy as np
from scipy.stats import norm

r=norm.rvs(size=200)

plt.hist(r,bins=20)

mu, sigma = norm.fit(r)

xx=np.linspace(r.min()-0.1, r.max()+0.1,100)
yy=norm.pdf(xx, loc=mu, scale=sigma)

plt.hist(r,bins=20, density=True)
plt.plot(xx,yy)

#%% QQplot
from scipy.stats import probplot



probplot(error, dist="norm", plot=plt)



from scipy.stats import skew, kurtosis
from scipy.stats import chi2

S=skew(error)

C=kurtosis(error, fisher=False) # 실제값. True시 다른 값이 나옴.

n, p = X.shape

JB = (n-p)/6*(S**2+(C-3)**2/4)

1-chi2.cdf(JB, df=2) #p-value of JB


colname = diabets.feature_names

col = 5

plt.scatter(X[:,col], error)

plt.xlabel(colname[col])
plt.ylabel('Residuals')


reg.fit(X, error**2)
e2_pred = reg.predict(X)
error_e2=error**2-e2_pred

SSE=sum(error_e2**2)
SSR=sum((e2_pred-np.mean(error**2))**2)

n,p = X.shape
MSE=SSE/(n-p-1)
MSR=SSR/p

f0 = MSR/MSE

from scipy.stats import f

1-f.cdf(f0,p,n-p-1) #p-value







r2=reg.score(X, error**2)
LM=n*r2

1-chi2.cdf(LM, p) #p-value




col=6
colname[col]
reg.fit(X[:,[col]], error**2)
r2=reg.score(X[:,[col]], error**2)
LM=n*r2

1-chi2.cdf(LM,1)




Xnew=X.copy()
Xnew[:,4]=Xnew[:,4]*100

reg2=LinearRegression()

reg.fit(X,y)
reg2.fit(Xnew,y)

reg.coef_
reg2.coef_

reg.score(X,y)
reg2.score(Xnew,y)








