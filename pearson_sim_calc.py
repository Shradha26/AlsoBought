# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 19:59:45 2017

@author: shrad
"""
import os
import pandas as pd
import numpy as np

os.chdir('C:\Users\shrad\Desktop\Recommendation_Systems\AlsoBought_1')

item_mat=pd.read_csv('item_mat.csv')
item_mat=item_mat.set_index(item_mat.iloc[:,0])
item_mat=item_mat.drop('movieId',1)
movies=pd.read_csv('movies_sub.csv')

print "Item-Item matrix loaded..."

movie_list=item_mat.index.values
sim_pear=pd.DataFrame(np.corrcoef(item_mat.iloc[:,:]),index=movie_list,columns=movie_list)

print "Done calculating similarities.."

head_list=['movieId','sim_movieId','sim_score']
sim_df=pd.DataFrame(index=range(100004),columns=head_list)
#because there are 10004 rows

index=0

for i in movie_list:
    count=0
    temp=pd.DataFrame(sim_pear.loc[i],index=movie_list)
    temp=temp.sort_values(by=[i],ascending=False,inplace=False)
    for j in temp.index.values:
        if i <> j:
            print "i="+str(i)+" "+"j="+str(j)
            sim_df.loc[index,'movieId']=i
            sim_df.loc[index,'sim_movieId']=j
            sim_df.loc[index,'sim_score']=sim_pear.loc[i,j]
            index+=1
            count+=1
            if(count==10):#the number of similarities recorded can be changed here
                break

sim_df=sim_df.dropna()
sim_df.to_csv('sim_acc_pearson.csv',',')

print "Ready..."