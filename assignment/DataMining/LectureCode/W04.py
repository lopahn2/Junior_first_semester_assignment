# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 21:22:20 2021

@author: lopah
"""

import pandas as pd
import numpy as np
from scipy import stats

petrol = pd.read_csv(r'C:\Users\lopah\Desktop\SeoulTEch\DataMining\petrol.csv')
X=petrol[['tax','income','highway','license']].values
n, p = X.shape
X=np.c_[np.ones(n),X]

XtX=np.matmul(X.T,X)
inv_XtX =  np.linalg.inv(XtX);
beta=np.matmul(np.matmul(inv_XtX,X.T), petrol[['consumption']].values).flatten()

y_pred = np.matmul(X, beta)
y_true = petrol['consumption'].values

SSE = np.sum((y_true - y_pred)**2)
MSE = SSE/(n-p-1)

se2_beta = MSE*inv_XtX

#beta 0 에 대한 test value
t=beta[0]/np.sqrt(se2_beta[0,0])
t1=beta[1]/np.sqrt(se2_beta[1,1])
t2=beta[2]/np.sqrt(se2_beta[2,2])
t3=beta[3]/np.sqrt(se2_beta[3,3])
t4=beta[4]/np.sqrt(se2_beta[4,4])

pvalue = (1-stats.t.cdf(np.abs(t), n-p-1))*2 #누적확률변수
pvalue1 = (1-stats.t.cdf(np.abs(t1), n-p-1))*2 
pvalue2 = (1-stats.t.cdf(np.abs(t2), n-p-1))*2 
pvalue3 = (1-stats.t.cdf(np.abs(t3), n-p-1))*2 
pvalue4 = (1-stats.t.cdf(np.abs(t4), n-p-1))*2 


#%% Simulation

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

b0=1
b1=2

betas=[]
repeat=100
reg = LinearRegression()

for i in range(repeat):
    xx=8*(np.random.random(100)-0.5) #-0.5~ 0.5
    yy=b0 + b1*xx+np.random.normal(loc=0, scale=1, size = 100) #scale = standard deviation , loc  =0  : normal distribution
    reg.fit(np.reshape(xx,(-1,1)), yy)
    betas.append([reg.intercept_] + list(reg.coef_))
    
betas=np.array(betas)

plt.hist(betas[:,0], bins=20)


mu, sigma = stats.norm.fit(betas[:,0])

xx=np.linspace(0.6,1.5,num=100)
#0.6~1.5까지 100개의 숫자만들기 

yy=stats.norm.pdf(xx,loc=mu, scale = sigma)

plt.hist(betas[:,0], bins=20 , density=True)
plt.plot(xx,yy)



#%% R^2

reg = LinearRegression()

reg.fit(petrol[['tax','income','highway','license']], petrol['consumption'])
r2 = reg.score(petrol[['tax','income','highway','license']], petrol['consumption'])

y_true=petrol['consumption'].values
y_pred=reg.predict(petrol[['tax', 'income','highway','license']])

SSE=np.sum((y_true-y_pred)**2)
SSR=np.sum((y_pred-np.mean(y_true))**2)

SST = np.sum((y_true-np.mean(y_true))**2)

SSR/SST
1-SSE/SST
r2

n, p = petrol[['tax','income','highway','license']].shape

adj_r2 = 1-((n-1)/(n-p-1))*(1-r2)

r2,adj_r2

#%%Compare R^2 and adj r^2

cols=['license', 'tax','income','highway']

r2=[]
adj_r2 = []

for i in range(len(cols)):
    reg.fit(petrol[cols[:i+1]], petrol['consumption'])
    r2.append(reg.score(petrol[cols[:i+1]],petrol['consumption']))
    adj_r2.append(1-((n-1)/(n-i-2))*(1-r2[-1]))
    


plt.plot(range(1,5), r2)
plt.plot(range(1,5), adj_r2)

#%% VIF

reg.fit(petrol[['income','highway','license']],petrol['tax'])
reg.score(petrol[['income','highway','license']],petrol['tax'])
vif=1/(1-reg.score(petrol[['income','highway','license']],petrol['tax']))


#%%
blood=pd.read_csv(r'C:\Users\lopah\Desktop\SeoulTEch\DataMining\bloodpress.csv', index_col=0)

blood.corr()
blood.cov()































