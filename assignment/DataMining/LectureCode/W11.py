# -*- coding: utf-8 -*-
"""
Created on Sun May 16 22:25:05 2021

@author: lopah
"""

from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np

n=500
#different normal distribution으로부터 샘플 생성
x1, y1 = datasets.make_blobs(n_samples = n, random_state=8)

#plt.scatter(x1[:,0],x1[:,1],c=y1)

x2, y2 = datasets.make_blobs(n_samples = n, random_state=170)
#plt.scatter(x2[:,0],x2[:,1],c=y2)
transformation=[[0.6,-0.6],[-0.4,0.8]]
x2=np.dot(x2,transformation)
#plt.scatter(x2[:,0],x2[:,1],c=y2)

x3, y3 = datasets.make_blobs(n_samples = n, cluster_std = [1.0,2.0,0.5],random_state=32)
#plt.scatter(x3[:,0],x3[:,1], c=y3)

x4, y4 = datasets.make_moons(n_samples = n,noise=0.1)
#noise가 작을수록, 선에 가까워짐.
#plt.scatter(x4[:,0],x4[:,1], c=y4)


#%% clustering algorithm

from sklearn.cluster import KMeans, AgglomerativeClustering


kmeans=KMeans(n_clusters = 3)
kmeans.fit(x1)

kmeans_laber = kmeans.labels_

#plt.scatter(x1[:,0],x1[:,1],c=kmeans_laber)


kmeans.n_clusters = 3
kmeans.fit(x2)

kmeans_laber = kmeans.labels_

#plt.scatter(x2[:,0],x2[:,1],c=kmeans_laber)

kmeans.fit(x3)
kmeans_laber = kmeans.labels_

#plt.scatter(x3[:,0],x3[:,1], c=kmeans_laber)

centroid=kmeans.cluster_centers_
#plt.scatter(centroid[:,0],centroid[:,1], marker='x', c='k')

x3_new, y3_new = datasets.make_blobs(n_samples=n, cluster_std = [1.0,2.0,0.5],random_state=11)
#plt.scatter(x3_new[:,0],x3_new[:,1], c=y3_new)


#%% predict
kmeans_label_new = kmeans.predict(x3_new)
#plt.scatter(x3_new[:,0],x3_new[:,1], c=kmeans_label_new)
#plt.scatter(centroid[:,0],centroid[:,1], marker='x', c='k')

kmeans.n_clusters = 2
kmeans.fit(x4)
kmeans_laber = kmeans.labels_
centroid=kmeans.cluster_centers_
#plt.scatter(x4[:,0],x4[:,1], c=kmeans_laber)
#plt.scatter(centroid[:,0],centroid[:,1],marker='x',c='k')


#%% agglomerative

aggl = AgglomerativeClustering(n_clusters = 3, affinity='euclidean',linkage='complete')
aggl.fit(x1)

aggl_label = aggl.labels_

#plt.scatter(x1[:,0],x1[:,1], c=aggl_label)

aggl.fit(x2)
aggl_label = aggl.labels_

#plt.scatter(x2[:,0],x2[:,1], c=aggl_label)

aggl.linkage = 'single'
aggl.fit(x2)
aggl_label = aggl.labels_

#plt.scatter(x2[:,0],x2[:,1], c=aggl_label)

aggl.linkage = 'ward'
aggl.fit(x2)
aggl_label = aggl.labels_

#plt.scatter(x2[:,0],x2[:,1], c=aggl_label)


aggl.linkage = 'complete'
aggl.fit(x3)
aggl_label = aggl.labels_

#plt.scatter(x3[:,0],x3[:,1], c=aggl_label)

aggl.n_clusters = 2
aggl.linkage = 'ward'
aggl.fit(x4)
aggl_label = aggl.labels_

#plt.scatter(x4[:,0],x4[:,1], c=aggl_label)


#%%hirechi---

x=[[30,10],[26,10],[16,16],[20,17],[19,18]]
aggl.fit(x)
aggl.children_
#cluster가 merge 되는 순서. index로 구분!


#%% gram 그리기

from scipy.cluster import hierarchy

Z=hierarchy.linkage(x1, method = 'single' , metric='euclidean')

fig = plt.figure(figsize=(10,6))
#hierarchy.dendrogram(Z)

cls_lable = hierarchy.cut_tree(Z, n_clusters = [3,5,7])
cls_lable = hierarchy.cut_tree(Z, height= 120)
np.unique(cls_lable.flatten())

#%% evaluation

from sklearn.metrics import silhouette_score, homogeneity_score, completeness_score, adjusted_rand_score

silhouette_score(x4,aggl_label)
#0보다 크니까 나쁜 건 아님!

iris = datasets.load_iris()
X= iris.data
y=iris.target

n_cls = 2
kmeans = KMeans(n_clusters=n_cls)
aggl = AgglomerativeClustering(n_clusters=n_cls)

kmeans.fit(X)
aggl.fit(X)

kmeans_label = kmeans.labels_
aggl_label = aggl.labels_

silhouette_score(X,kmeans_label)
silhouette_score(X,aggl_label)



homogeneity_score(y, kmeans_label)
completeness_score(y, kmeans_label)
adjusted_rand_score(y, kmeans_label)

homogeneity_score(y, aggl_label)
completeness_score(y, aggl_label)
adjusted_rand_score(y, aggl_label)




kmeans.inertia_

inertia=[]

for n_cls in range(2,11):
    kmeans.n_clusters = n_cls
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)
    
#plt.plot(range(2,11), inertia)

s=[]
for n_cls in range(2,11):
    kmeans.n_clusters = n_cls
    kmeans.fit(x1)
    s.append(silhouette_score(x1,kmeans.labels_))

plt.plot(range(2,11), s)


#%%silhouette coefficient

from sklearn.metrics import silhouette_samples


kmeans.n_clusters = 3
kmeans.fit(x2)
kmeans_label = kmeans.labels_

s = silhouette_samples(x2, kmeans_label)

n_cls = 3
count = 0 

fig = plt.figure(figsize=(6,8))
ax = plt.gca()
colors=plt.cm.hsv(np.arange(n_cls)/n_cls)
ylabel_pos = []

for i in range(n_cls):
    ind=np.where(kmeans_label == i)[0]
    sel_s = s[ind]
    sel_s.sort()
    ax.fill_betweenx(np.arange(count, count+len(ind)), 0 ,sel_s, fc=colors[i], ec= colors[i], alpha = 0.7)
    ylabel_pos.append(count+len(ind)/2)
    count +=len(ind)
    
plt.yticks(ylabel_pos, [str(i) for i in range(n_cls)])
plt.ylabel('Cluster label')
plt.xlabel('The silhouette coefficient values')
ax.axvline(x=np.mean(s), color = 'r', ls='--')

























