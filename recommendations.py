# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 20:29:52 2017

@author: shrad
"""

import os
import pandas as pd

os.chdir('C:\Users\shrad\Desktop\Recommendation_Systems\AlsoBought_1')


#sim_df=pd.read_csv('sim_df.csv')
sim_df=pd.read_csv('sim_acc_pearson.csv')
#sim_df=pd.read_csv('sim_acc_cosine.csv')
movies=pd.read_csv('movies_sub.csv')
ratings=pd.read_csv('ratings_sub.csv')

def AlsoViewed(user_id,movie_id):
    simlist=sim_df.loc[sim_df['movieId']==movie_id]['sim_movieId']
    rated=ratings.loc[ratings['userId']==user_id].iloc[:,2]
    simlist=list(set(simlist).difference(set(rated)))
    
    print "People who viewed this movie ("+movies.loc[movies['movieId']==movie_id]['title']+") also viewed:"
    print "\n"*3
    
    #out_file=open("output_cosine_"+str(user_id)+"_"+str(movie_id)+".txt",'w')
    out_file=open("output_pear_"+str(user_id)+"_"+str(movie_id)+".txt",'w')
    
    for item in simlist:
        text=movies.loc[movies['movieId']==item].iloc[:,1:4]
        out_file.write(str(text))
        
    out_file.close()
        

AlsoViewed(254,9)