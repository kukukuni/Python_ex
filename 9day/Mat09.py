# Mat09.py
import matplotlib.pyplot as plt
import numpy as np

학생이름 = ['Jane','Alice','Tom','John']
점수 = [85,100,75,60]

#plt.figure(figsize=(10,6))
#plt.bar(학생이름,점수)
a = np.arange(len(학생이름))
#sc1= plt.subplot()
fig,sc1 = plt.subplots()
sc1.bar(a,점수,color='green')
plt.show()