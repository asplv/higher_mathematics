import numpy as np
import matplotlib.pyplot as plt

def cos_show():
	x = np.linspace(0,10,100)
	k=1
	plt.plot(x, np.cos(k*x), color='g', marker = 'o')
	k=2
	plt.plot(x, np.cos(k*x), color='b', marker = 'o')
	plt.show()

cos_show()

