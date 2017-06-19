# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 21:56:58 2017

@author: shrad
"""

#imports
import os
import pandas as pd
import numpy as np

#changing the working directory
os.chdir('C:\Users\shrad\Desktop\Recommendation_Systems\AlsoBought_1')

#loading the datasets
ratings=pd.read_csv('ratings.csv')
movies=pd.read_csv('movies.csv')
print "Data Loaded..."

#record the movies that have not been rated by any user
mId=[]

for m in ratings['movieId']:
    if m not in mId:
        mId.append(m)
        
not_rated=[]
for m in movies['movieId']:
    if m not in mId:
        not_rated.append(m)

print "Recognized movies that have not been rated.."        

#remove the not rated items from the data frame
movies_sub=movies.loc[movies['movieId'].isin(not_rated)]
movies_new=movies.merge(movies_sub,how='left',indicator=True)
movies=movies_new[movies_new['_merge']=='left_only']
ratings=ratings.iloc[:,0:2]
users=ratings.groupby('userId').groups.keys()
print "Finished subsetting data by removing unrated items.."

movies.to_csv('movies_sub.csv',sep=',')
ratings.to_csv('ratings_sub.csv',sep=',')

#dataframe for item-item matrix
movielist=movies.iloc[:,0]
item_mat=pd.DataFrame(0,index=users,columns=movielist) #row and column indexes are movieIds

for u in users:
    print u
    rated=ratings.loc[ratings['userId']==u].iloc[:,1:2]
    rated=rated.squeeze().tolist()
    i=0
    while i < len(rated):
        item_mat.loc[u,rated[i]]=1
        i+=1            
                    
print "Calculated counts"

df_asint = item_mat.astype(int)
coocc = df_asint.T.dot(df_asint)
np.fill_diagonal(coocc.values, 0)

coocc.to_csv('item_mat.csv',sep=',')
print "Created item_item matrix" 