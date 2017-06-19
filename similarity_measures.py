# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 19:45:41 2017

@author: shrad
"""
from math import sqrt

class Similarity():
    
    def jaccard_similarity(self,x,y):
        intersection_cardinality=len(set.intersection(*[set(x),set(y)]))
        union_cardinality=len(set.union(*[set(x),set(y)]))
        return intersection_cardinality/float(union_cardinality)
    
    def average(self,x):
        assert len(x)>0
        return float(sum(x))/len(x)

    
    def pearson_similarity(self,x,y):   
     #An expression is tested, and if the result comes up false, an exception is raised
        assert len(x)==len(y)
        #if x==y:
        #    return 1
        n=len(x)
        assert n>0
        avg_x=self.average(x)
        avg_y=self.average(y)
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

