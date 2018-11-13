import numpy as np
import matplotlib.pyplot as plt

s = [u'^', u'+', u'o']
col = ['r','r','g']
x = np.array([1,2,3])
y = np.array([4,5,6])

for _s, c, _x, _y in zip(s, col, x, y):
    print(_s)
    print(c)
    print(_x)
    print(_y)
    plt.scatter(_x, _y, marker=_s, c=c)

plt.xlim(0, 4)
plt.ylim(0, 8)

plt.show()