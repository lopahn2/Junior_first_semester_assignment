# -*- coding: utf-8 -*-
"""
Created on Fri May 28 02:11:19 2021

@author: lopah
"""

from apyori import apriori

transactions = [['beer','nut'], ['beer','cheese']]
result = list(apriori(transactions))

import urllib
f = urllib.request.urlopen('https://drive.google.com/uc?export=download&id=1kxhLR1fTGq-Ci8FxP3toCShA6CZdNS_D')

data=[]

for l in f:
    l=l.decode('utf-8')
    data.append(l.strip().split(","))
    
results = list(apriori(data, min_support=0.3, min_confidence = 0.7))




import pandas as pd

mushroom = pd.read_csv((f'https://drive.google.com/uc?export=download&id=1GjJFiGX_QGoTqfo85n1mjrXP7pNSIWw_'))

for c in mushroom.columns[1:]:
    mushroom[c] = mushroom[c].apply(lambda x : '%s_%s'%(c,x))
    
results = list(apriori(mushroom.values, min_support=0.3, min_confidence = 0.8))


sel_results=[x for x in results if len(x[0])>1]
sel_results[0]

rules = pd.DataFrame(columns=['condition','result','support','confidence','lift'])

count = 0
for i, r in enumerate(sel_results):
    x=[o for o in r[2]]
    s= r[1]
    for xx in x:
        rules.loc[count]=[xx[0],xx[1],s,xx[2],xx[3]]
        count +=1
        
        
r1 = rules[rules['result']=={'p'}]
r2 = rules[rules['result']=={'e'}]

r1 = r1.sort_values('confidence',ascending=False)
r1['condition'] = r1['condition'].apply(lambda x: ','.join(list(x)))
r1.iloc[0,0]



























