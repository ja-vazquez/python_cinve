# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:28:07 2017

@author: Andres
"""
from time import time
a=1
h=2
k=0
ti=time()
while h <= 4000000:
    if h%2==0:
        k+=h
        temporal=h
        h=h+a
        a=temporal
print (total)
tf=time()
T=tf-ti
print (T)
