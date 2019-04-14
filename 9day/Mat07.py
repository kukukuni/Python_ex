# Mat07.py

import matplotlib.pyplot as plt
import numpy as np

a = np.random.normal(loc=0,scale=1,size=1000)
b = np.random.normal(loc=5,scale=0.5,size=1000)
c = np.random.normal(loc=10,scale=2,size=1000)
plt.figure(figsize=(10,6))
plt.plot(a,label='a')
plt.plot(b,label='b')
plt.plot(c,label='c')
plt.legend()
plt.show()