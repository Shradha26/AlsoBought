# -*- coding: utf-8 -*-
"""
Created on Mon May 29 16:47:34 2017

@author: MAHE
"""
#imports
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#changing the working directory
os.chdir('C:\Users\shrad\Desktop\Recommendation_Systems\AlsoBought_1')

#loading the MovieLens dataset
links=pd.read_csv('links.csv')
movies=pd.read_csv('movies.csv')
ratings=pd.read_csv('ratings.csv')
tags=pd.read_csv('tags.csv')

#testing if the data has been loaded properly
print links   #index based subsetting

#describing the data
print links.describe()

#playing around with the sequence
#i=1
#for id in links['movieId']:
#    if id==i:
#        i=i+1
#    else:
#        break

#print "Value :"+str(i)
#print links.iloc[30:40,:]

#exploring movies.csv
print "Summary of movies.csv"
print movies.describe()
print movies.iloc[10:40,:]

genres={}

for item in movies['genres']:
    words=[]
    words=item.split('|')
    
    for word in words:
        if word not in genres:
            genres[word]=0
        else:
            genres[word]+=1
                  
print "Size"+str(len(genres))

key=np.array(range(1,21))
value=np.array(genres.values())
#print key
my_xticks=genres.keys()
plt.xticks(key,my_xticks)
plt.plot(key,value)
plt.show()

maximum=max(genres,key=genres.get)
print maximum+" "+str(genres[maximum])
minimum=min(genres,key=genres.get)
print minimum+" "+str(genres[minimum])

#need to check code
#for item in movies:
#    if '(no genres listed)' in item[1]:
#        print item

#exploring ratings.csv
print "Summary of ratings.csv"
print np.shape(ratings)

#finding the movies that have not been rated
print ratings.loc[ratings['rating'].isnull()]

mId=[]

for m in ratings['movieId']:
    if m not in mId:
        mId.append(m)
        

#smId=sorted(mId)
a=set()
for m in movies['movieId']:
    if m not in mId:
        a.add(m)

print a #set containing movies that have not been rated

b=set()

temp=movies.loc[movies['genres']=='(no genres listed)']
    
for i in temp['movieId']:
    b.add(i)
    
print "Size of set:"+str(len(a.intersection(b)))
