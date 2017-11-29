
# coding: utf-8

# # Probabilidad

# In[9]:


#numero aleatorio
import random
Num_aleatorio = random.random()
print(Num_aleatorio)


# In[6]:


#numero aleatorio entero
import random
Num_aleatorio= random.randint(1,10)
print(Num_aleatorio)


# In[2]:


import numpy as np
np.random.random(10)


# In[13]:


#lanzamiento de un dado
import random
Num_dado=random.randint(1,6)
print(Num_dado)


# In[18]:


#lanzamiento de un dado N veces
import random
[random.randint(1,6) for _ in range(10)]
                    


# In[21]:


#desiciones
from random import choice

mascota = ["Gato", "Perro", "Conejo", "Serpiente", "Tarantula", "Pez"]

print(choice(mascota))


# In[24]:


from numpy.random import choice

mascota = ["Gato", "Perro", "Conejo", "Serpiente", "Tarantula", "Pez"]

x1 = choice(mascota, size=2)
print(x1)
x2 = choice(mascota, size=(4))
print(x2)


# In[34]:


import numpy as np # importando numpy
datos=np.random.randn(5,5)
datos


# In[36]:


np.mean(datos) #media aritmetica


# In[37]:


np.median(datos) #mediana


# In[39]:


np.std(datos) #desviacion estandar


# In[40]:


np.var(datos) #varianza


# In[44]:


# Ejemplo situación 2 La coincidencia de cumpleaños
prob = 1.0
asistentes =5

for i in range(asistentes):
    prob = prob * (365-i)/365

print(1-prob)

