# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 17:06:15 2021

@author: lopah
"""

from sklearn.naive_bayes import BernoulliNB, CategoricalNB, MultinomialNB, GaussianNB
import pandas as pd
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt


iris=datasets.load_iris()
X=iris.data
y=iris.target

X>X.mean(0)
Xbin=(X>X.mean(0))*1 #False = 0 , True = 1

#%%Bernoulli
bernNB = BernoulliNB()
#bernNB = BernoulliNB(alpha=2) 알파값 조정가능
bernNB.fit(Xbin,y)

bernNB.class_log_prior_
np.exp(bernNB.class_log_prior_)
#Size of three classes are all same. so there are same class_prior

#Check the parameter
bernNB.feature_log_prob_
#col=different input feature    row= different class

#actual parameter
np.exp(bernNB.feature_log_prob_)
#모두 0인경우 class도 0여야 하지만 smoothing parameter때문에 0.0198```가 되는거임

bernNB.class_count_
bernNB.feature_count_ # count x = 1


#%%Gaussian
gausNB=GaussianNB()
gausNB.fit(X,y)

gausNB.theta_ #mean of Normaldistribution
gausNB.sigma_ #variance

gausNB.score(X,y) #calculate accuracy
bernNB.score(Xbin,y)



#%%draw histogram

for c in np.unique(y):
    plt.hist(X[y==c,0],bins=10,label=str(c),alpha=0.7)
plt.legend()


#%%Categorical
#for object variables. not numeric
car = pd.read_csv('https://drive.google.com/uc?export=download&id=1wFAkAmsIBiLQXXejiFVJr_TqUbm9HMDP')
X=car.drop('class',axis=1)
y=car['class']

from sklearn.preprocessing import LabelEncoder
#카테고리를 숫자로 인코딩해줌

enc = LabelEncoder()
enc.fit(y)
enc.classes_ #sorted as alphabet order
enc.transform(y[-10:]) #index number로 encoding

enc_dict = dict()
for c in X.columns:
    enc_dict[c]=LabelEncoder()
    enc_dict[c] = enc_dict[c].fit(X[c])

Xconv=pd.DataFrame(columns=X.columns)
for c in X.columns:
    Xconv[c] = enc_dict[c].transform(X[c])
Xconv.dtypes

#data type change to numeric

catNB=CategoricalNB()
catNB.fit(Xconv,y)

catNB.class_log_prior_
np.exp(catNB.class_log_prior_)
y.value_counts()
catNB.feature_log_prob_

catNB.feature_log_prob_[0] #buying price's feature
np.exp(catNB.feature_log_prob_[0])

enc_dict['buying'].classes_

#%%logistic regression

y_pred = catNB.predict(Xconv)
y_prob= catNB.predict_proba(Xconv)
#[acc, good, unacc, vgood] 순서로 표현

#%%multinomial

spam = pd.read_csv('https://drive.google.com/uc?export=download&id=1l6gUFvs4PNoY2OVg44hCNmOREfEsx2qX')
X=spam.drop('target', axis=1)
y=spam['target']
#1 is spam

y.value_counts()

multiNB=MultinomialNB()
multiNB.fit(X,y)

multiNB.class_log_prior_
np.exp(multiNB.class_log_prior_)
#spam probability
multiNB.feature_log_prob_
#[parameter class 0, parameter multi class 1]
p_word=np.exp(multiNB.feature_log_prob_)
#number is probabilty of spam
p_word2=pd.DataFrame(np.exp(multiNB.feature_log_prob_),columns=X.columns)
#probability가 높은 녀석이 스팸에 사용되는 단어일 확률이 높다!
p_word.sum(1) # always 1








