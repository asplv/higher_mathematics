import numpy as np
import itertools
import math

def ckn(k, n):
	return math.factorial(n)/(math.factorial(k)*math.factorial(n-k))

counter, repetitions = 0, 100000

a = np.random.randint(0, 2, repetitions)
b = np.random.randint(0, 2, repetitions)
c = np.random.randint(0, 2, repetitions)
d = np.random.randint(0, 2, repetitions)
x = a + b + c + d

for i in range(0, repetitions):
	if x[i] == 2:
		counter = counter + 1
print("actual", counter/repetitions)

p = 0.5
q = 0.5
n = 4
k = 2
print("expected", ckn(k, n)*(p**k)*(q**(n-k)))






counter, repetitions = 0, 100000

p = 0.5
q = 0.5
n = 5
k = 3

x = np.zeros(repetitions)
for i in range(n):
	x = x + np.random.randint(0, 2, repetitions)

for i in range(0, repetitions):
	if x[i] == 3:
		counter = counter + 1

print("actual", counter/repetitions)
print("expected", ckn(k, n)*(p**k)*(q**(n-k)))
