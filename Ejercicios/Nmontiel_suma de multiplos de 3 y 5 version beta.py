# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:34:04 2017

@author: Andres
"""
"""
Si enumeramos todos los números naturales por debajo de 10 
que son múltiplos de 3 o 5, obtenemos 3, 5, 6 y 9. 
La suma de estos múltiplos es 23.
Encuentra la suma de todos los múltiplos de 3 o 5 debajo de 1000
"""
from time import time
def miniMultiplos(n,N):
 p=int((N-1)/n)
 sumatoria=int(n*(p*(p+1))/2)
 return sumatoria 
def multiplos3y5(N):
 return miniMultiplos(3,N)+miniMultiplos(5,N)-miniMultiplos(15,N)
ti=time()
print (multiplos3y5(1000))
tf=time()
T=tf-ti
print(T)
