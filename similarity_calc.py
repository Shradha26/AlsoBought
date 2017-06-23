# -*- coding: utf-8 -*-
"""
Created on Tue Jun 06 17:44:55 2017

@author: shrad
"""

#imports 
import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

#changing the working directory
os.chdir('C:\Users\shrad\Desktop\Recommendation_Systems\AlsoBought_1')

#loading required dataframes
item_mat=pd.read_csv('item_mat.csv')
movies=pd.read_csv('movies_sub.csv')
ratings=pd.read_csv('ratings_sub.csv')

print "Data Loaded..."


item_mat=item_mat.set_index(item_mat.iloc[:,0])
item_mat=item_mat.drop('movieId',1)
movie_list=item_mat.index.values

print item_mat.iloc[0:5,0:5]


A=np.array(item_mat)


similarities=cosine_similarity(A)

print len(movie_list)

sim_mat=pd.DataFrame(similarities,index=movie_list,columns=movie_list)

#sim_mat.to_csv("simcosine.csv",sep=",")
    
print "Finished Similarity Calculations"

head_list=['movieId','sim_movieId','sim_score']
sim_df=pd.DataFrame(index=range(100004),columns=head_list)

index=0
for i in movie_list:
    print i
    count=0
    temp=pd.DataFrame(sim_mat.loc[i],index=movie_list)
    temp=temp.sort_values(by=[i],ascending=False,inplace=False)
    for j in temp.index.values:
        if i <> j:
            sim_df.loc[index,'movieId']=i
            sim_df.loc[index,'sim_movieId']=j
            sim_df.loc[index,'sim_score']=sim_mat.loc[i,j]
            index+=1
            count+=1
            if(count==10):#the number of similar matrices can be recorded here
                break
            
            
sim_df=sim_df.dropna()
sim_df.to_csv('sim_acc_cosine.csv',',')

print "All set! Good to go.."