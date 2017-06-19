# -*- coding: utf-8 -*-
"""
Created on Mon Jun 05 15:08:58 2017

@author: shrad
"""

import os
import pandas as pd
import pickle
from  math import sqrt


os.chdir('C:\Users\shrad\Desktop\Recommendation_Systems\AlsoBought_1')

#loading required dataframes
movies=pd.read_csv('movies_sub.csv')
ratings=pd.read_csv('ratings_sub.csv')
item_mat=pd.read_csv('item_mat.csv')

print "Loaded Data.."
#create similarity matrix
#sim_mat=pd.DataFrame(0,index=movies.iloc[:,0],columns=movies.iloc[:,0]) 
sim_mat=dict.fromkeys(movies.iloc[:,1],pd.Series(index=movies.iloc[:,1]))
  
#function for pearsonn correlation
def average(x):
    assert len(x)>0
    return float(sum(x))/len(x)

def pearsoncorr(x,y):
     #An expression is tested, and if the result comes up false, an exception is raised
     assert len(x)==len(y)
     if x==y:
         return 1
     n=len(x)
     assert n>0
     avg_x=average(x)
     avg_y=average(y)
     a=0
     b=0
     c=0
     d=0
     num=0
    
     for idx in range(n):
        a=x[idx]-avg_x
        b=y[idx]-avg_y
        num+=a*b
        c+=a*a
        d+=b*b
        
     return num/sqrt(c*d)


def calc_sim(sim_mat,item_mat):
    
    for i in movies.iloc[:,1]:
        for j in movies.iloc[:,1]:
            temp=pearsoncorr(item_mat.loc[item_mat['movieId']==i,:].squeeze().tolist(),item_mat.loc[item_mat['movieId']==j,:].squeeze().tolist())
            sim_mat[i][j]=temp
            sim_mat[j][i]=sim_mat[i][j]
            print "i="+str(i)+" j="+str(j)    



#calc_sim(sim_mat,item_mat)
#print sim_mat

def save_sim_mat(sim_mat):
    f=open('sim_mat.pkl','w')   
    pickle.dump(sim_mat,f)  
    f.close()

#print "Similarity matrix created.."            

#sorting similarities in descending order
def sortSimilarities():
    idx=0
    temp=movies.iloc[:,0]
    #temp.iloc[1]
    n=len(temp)
    while idx < n:
        sim_mat[temp.iloc[idx]]=sim_mat[temp.iloc[idx]].sort_values(ascending=False)
        idx+=1
        
 
#sortSimilarities()
#print sim_mat
#print "Sorted Similarities.."