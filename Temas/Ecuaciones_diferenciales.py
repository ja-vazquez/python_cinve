
# coding: utf-8

# # Ecuaciones diferenciales

# In[2]:


from sympy import init_printing, Symbol, Function, Eq, dsolve, diff
init_printing()    ##sympy es una biblioteca que contiene muchas caracteristicas matematicas muy simples de manejar con tan solo llamarlas 
#llamamos la caracteristica: symbol, function, eq, dsolve, diff, etc
x = Symbol("x")    #nombramos a nuestras variables y funciones
f = Function("f")

eq = Eq(f(x).diff(x), f(x))      #eq sirve para plasmar nuestra ecuacion en lenguaje de python
eq


# In[37]:


dsolve(eq,f(x))   #para resolver la ecuacion diferencial, solo ponemos dsolve y lo que queremos resolver


# # Oscilador Armónico

# $$x''+ ([w_0] ^2)x=0$$

# In[12]:


from sympy import init_printing, Symbol, Function, Eq, dsolve, diff
init_printing()         #como queremos resolver la ecuacion diferencial del oscilador armonico llamamos a las caracteristicas que vamos a usar 

w_0 = Symbol("w_0")   #definimos w_0 como una variable
t = Symbol("t")       #definimos t como una variable
x= Function("x")      #definimos x como una funcion 

eq = Eq(x(t).diff(t).diff(t),(w_0)**2*x(t))    # x(t).diff(t).diff(t) significa que escogemos a x como funcion de t, la cual estará derivada 2 veces
eq


# In[71]:


dsolve(eq,x(t))       #resolvemos la ecuación

