import numpy as np
from numpy import pi
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Figure
fig = plt.figure()
fig.set_dpi(300)
ax1 = fig.add_subplot(1,1,1)

#Information
k = 3
L = pi

#Initial conditions
x0 = np.linspace(0,pi,5000)
t0 = 0
temp0 = 10

#Time
dt = 0.01


#Heat
def u(x,t):
    return temp0 + np.exp(-k*t)*np.sin(x)

#temporal derivative
def dertem_u(x,t):
    return np.array([-k*np.exp(-k*t)*np.sin(x)])

a = []
t = []
for i in range(120):
    value = u(x0 ,t0) + dertem_u(x0,t0)[0]*dt
    t.append (t0)
    t0 = t0 + dt
    a.append(value)

k = 0
def animate(i):         
    global k            
    x = a[k]            
    k += 1              
    ax1.clear()
    plt.plot(x0,x,color='red',label='Temperature at each x')
    plt.plot(0,0,color='white',label='Elapsed time '+str(round(t[k],2)))
    plt.grid(True)
    plt.ylim([temp0-2,2.5*5])
    plt.xlim([0,L])
    plt.title('Heat equation')
    plt.legend()
    
anim = animation.FuncAnimation(fig,animate,frames=360,interval=50)
plt.show()
