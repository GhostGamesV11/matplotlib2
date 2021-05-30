import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


fig=plt.figure()
ax=fig.gca(projection='3d')
t=np.linspace(0,2*np.pi,100)
z=t
x=np.sin(z)
y=2*np.cos(z)
ax.plot(x,y,z,label='zadanie 1')
ax.legend()
plt.show()