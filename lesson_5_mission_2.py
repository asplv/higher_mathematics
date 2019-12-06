import random

# проверим теорему сложения
# т.е. вероятность того что 1 или 2 должна быть 1/37 + 1/37

def spinRoulette():
	return random.randint(0, 36)

counter = 0
for i in range(int(1e6)):
	value = spinRoulette()
	counter += 1 if (value == 1 or value == 2) else 0

print(counter/1e6)
print(2/37)





import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

selections = [np.random.rand(10000) for i in range(10)]

num_bins = 100
n, bins, patches = plt.hist(sum(selections), num_bins)
plt.xlabel('sum')
plt.ylabel('Probability')
plt.title('Histogram')

plt.show()
