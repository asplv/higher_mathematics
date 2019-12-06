import numpy as np
import matplotlib.pyplot as plt

n = 100
r = 0.7
x = np.random.rand(n)
y = r*x + (1-r)*np.random.rand(n)

plt.plot(x, y, 'o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

a = (np.sum(x)*np.sum(y) - n*np.sum(x*y))/(np.sum(x)*np.sum(x) - n*np.sum(x*x))
b = (np.sum(y) - a*np.sum(x))/n

tmp = np.vstack([x, np.ones(len(x))]).T
a1, b1 = np.linalg.lstsq(tmp, y)[0]
print(a, b)
print(a1, b1)

plt.plot([0, 1], [b, a+b])
plt.show()

xm = np.sum(x)/n
ym = np.sum(y)/n
R = np.sum((x - xm)*(y - ym)) / (np.sum((x - xm)**2)*np.sum((y - ym)**2))**0.5
print(R)
