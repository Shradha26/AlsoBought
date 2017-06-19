# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 19:52:08 2017

@author: shrad
"""

import os
import pandas as pd

os.chdir('C:\Users\shrad\Desktop\Recommendation_Systems\AlsoBought_1')

ratings=pd.read_csv('ratings_sub.csv')
users=ratings.groupby('userId').groups.keys()
movies=pd.read_csv('movies_sub.csv')
sim_df=pd.read_csv('sim_acc_cosine.csv')

#print movies.loc[movies['movieId']==3]['title']

def GetSimilarMovies(movie_id):
    simlist=list(sim_df.loc[sim_df['movieId']==movie_id]['sim_movieId'])
    return simlist

def UsersWhoWatched(movie_id):
    ulist=[]
    rated=pd.DataFrame()
    for u in users:
        rated=ratings.loc[ratings['userId']==u].iloc[:,2]
        if movie_id in rated.squeeze().tolist():
            ulist.extend([u])
    
    return ulist

def GetPeopleForEachMovie(movie_id):
    sim_mov=sim_df.loc[sim_df['movieId']==movie_id]['sim_movieId']
    fname=open("List9.txt","w")
    ll=UsersWhoWatched(movie_id)
    for r in sim_mov:
        fname.write("\n"+str(getMovieFromId(r)))
        temp=UsersWhoWatched(r)
        fname.write("\nTotal="+str(len(temp)))
        fname.write(str(temp))
        fname.write("\nCommon="+str(len(set(temp).intersection(set(ll)))))
        
    fname.close()

def MoviesWatchedByUsers(movie_id):
    fname=open("AllUserAndMovies_"+str(movie_id)+".txt","w")    
    rated=pd.DataFrame()
    for u in users:
        rated=ratings.loc[ratings['userId']==u].iloc[:,2]
        rated_list=rated.squeeze().tolist()
        if movie_id in rated_list:
            #print "User="+str(u)+":"
            fname.write("User="+str(u)+":")
            for r in rated_list:
                #print getMovieFromId(r)
                fname.write(str(getMovieFromId(r)))
                
    fname.close()

            
            
def getMovieFromId(movie_id):
    return movies[movies['movieId']==movie_id]['title']


#GetPeopleForEachMovie(9)
print UsersWhoWatched(40)