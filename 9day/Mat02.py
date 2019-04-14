# Mat02.py

import matplotlib.pyplot as plt
a = [10,20,30,40]
b = range(0,100)
c = [1,2,3,4,5,4,2,1,3]
d = range(0,11)
e = [i**2 for i in d]

plt.plot(d,e,'gs') # (x축,y축,그래프표현형태)
plt.show()