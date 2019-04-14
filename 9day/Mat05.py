# Mat05.py

import matplotlib.pyplot as plt
import numpy as np

a = np.arange(0,9)
b = [1,4,6,9,5,2,7,3,8]

plt.figure(figsize=(10,6))
plt.plot(a,b,
         color='red',linestyle='dashed',
         marker='o',markerfacecolor='blue',
         markersize=12)
plt.xlim([3,7])
plt.ylim([2.5,7.5])
plt.show()
