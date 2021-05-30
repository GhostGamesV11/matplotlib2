import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#zad 1

fig=plt.figure()
ax=fig.gca(projection='3d')
t=np.linspace(0,2*np.pi,100)
z=t
x=np.sin(z)
y=2*np.cos(z)
ax.plot(x,y,z,label='zadanie 1')
ax.legend()
plt.show()


#zad 2

def randrange(n,min,max):
    return (max-min)*np.random.rand(n)+min
fig = plt.figure()
ax=fig.add_subplot(111, projection="3d")
n=100
for c,m,zlow,zhigh in [("r","o",100, 60), ("b", "^", 80, 40),
                        ("g", "v", 60, 20), ("y", "s", 40, 10),
                        ("m", "*", 100, 10)]:
    xs=randrange(n,0,50)
    ys=randrange(n,0,200)
    zs=randrange(n,zlow, zhigh)
    ax.scatter(xs,ys,zs,c=c,marker=m)

ax.set_xlabel("x label")
ax.set_ylabel("y label")
ax.set_zlabel("z label")
plt.show()


#zad 3

fig=plt.figure()
ax=fig.gca(projection="3d")
X=np.arange(-5, 5, 0.25)
Y=np.arange(-5, 5, 0.25)
X,Y=np.meshgrid(X, Y)
R=np.sqrt(X**2+Y**2)
Z=np.sin(R)
lista=["PuOr","hot","coolwarm","spring","cool"]
kolor=np.random.choice(lista)
surface=ax.plot_surface(X,Y,Z,cmap=kolor,linewidth=0,antialiased=False)
ax.set_zlim(-1.01,1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter("%.02f"))
fig.colorbar(surface,shrink=0.5,aspect=5)
plt.show()


#zad 4

fig=plt.figure(figsize=(15,5))
ax1=fig.add_subplot(151,projection="3d")
ax2=fig.add_subplot(152,projection="3d")
ax3=fig.add_subplot(153,projection="3d")
ax4=fig.add_subplot(154,projection="3d")
ax5=fig.add_subplot(155,projection="3d")
_x=np.arange(4)
_y=np.arange(5)
_xx,_yy=np.meshgrid(_x,_y)
x,y=_xx.ravel(),_yy.ravel()
top=x+y
bottom=np.zeros_like(top)
width=depth=1
ax1.bar3d(x,y,bottom,width,depth,top,shade=True,color="r")
ax2.bar3d(x,y,bottom,width,depth,top,shade=False,color="y")
ax3.bar3d(x,y,bottom,width,depth,top,shade=True,color="c")
ax4.bar3d(x,y,bottom,width,depth,top,shade=False,color="b")
ax5.bar3d(x,y,bottom,width,depth,top,shade=True,color="w")
plt.show()