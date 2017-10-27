
# coding: utf-8

# # TAREA COSMO

# # Problema1: multiplos de 3 y 5

# In[2]:


def multiple(valor,multiple):   #se define la operacion multiplo
    mult = valor % multiple     #donde i sera el valor de del rango y multiple sera el numero el cual queramos que sea multiplo
    if mult==0:
        return True              #condicion para saber si un numero es multiplo o no
    else:
        return False
    
multiples_3_5=[]               #array de los numeros que son multiplos de 3 y 5

    
for i in range (1,1000):        #rango del cual queremos saber los nuemros multiplos de 3 y 5
    if multiple(i,3):
        multiples_3_5.append(i)     #si i es multiplo de 3 se guarda en el array
        
    if multiple(i,5):
        multiples_3_5.append(i)     #si i es multiplo de 5 se guarda en el array
        
print "los multiplos de 3 y 5 son:", multiples_3_5


# In[65]:


total=0             
for i in range(0,1000):      #rango de i el cual queremos saber si es multiplo de 3 y 5
    if i%3==0 or i%5==0:   #condicion de multiplicidad
        total+=i           #suma los digitos que cumplen la condicion
print total


# # Problema 2: Fibonacci

# In[63]:


#determinar la suma de los numeros pares de la serie de Fibonacci

a, b = 1, 1  #definimos los 2 primeros numeros de la serie
total = 0    
while a <= 4000000:   #realizamos el ciclo en el rango deseado
    if a % 2 == 0:    #condicion de numero par
        total += a    #se realiza la suma de los numeros pares
    a, b = b, a+b   #se generan los nuevos elementos segun la definicion de la serie de fibonacci

print total

