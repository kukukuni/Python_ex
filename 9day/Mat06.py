# Mat06.py

import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0,10)
b = np.array([9,4,6,9,5,2,7,1,3,2])

plt.figure(figsize=(10,6))
plt.scatter(x=a,y=b,s=100,c=a,marker='>') #산점도
plt.colorbar()
plt.show()