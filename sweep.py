
import numpy as np
import time
from math import*
import matplotlib.pyplot as plt
def sweep(a, b, c, f, n):
    alpha = np.array([0.0] * (n + 1))
    beta = np.array([0.0] * (n + 1))
    for i in range(n):
        d = a[i] * alpha[i] + b[i]
        alpha[i + 1] = -c[i] / d
        beta[i + 1] = (f[i] - a[i] * beta[i]) / d
    x = np.array([0.0] * n)
    x[n - 1] = beta[n]
    for i in range(n - 2, -1, -1):
        x[i] = alpha[i + 1] * x[i + 1] + beta[i + 1]
    return x
  
k = 5
sweep_time = np.zeros(k)
library_time = np.zeros(k)
for i in range(1,k+1):
	n = i*1000
	a = np.random.rand(n)
	b = np.random.rand(n)
	c = np.random.rand(n)
	f = np.random.rand(n)
	A = np.zeros((n,n))


	for m in range(n):
		for k in range(n):
			if m == k:
				A[m][m] = b[m]
				if k - 1 >=0:
					A[m][k-1] = a[k]
				if k + 1 < n:
					A[m][k + 1] = c[k]


	t1 = time.time()
	x = sweep(a, b, c, f, n)
	t2 = time.time() - t1
	sweep_time[i-1] = t2

	t1 = time.time()
	x_compare = np.linalg.solve(A,f)
	t2 = time.time() - t1
	library_time[i-1] = t2

	print('for n =',n,'||x - x_compare|| = ', max(x_compare - x))
plt.plot(sweep_time)
plt.plot(library_time)
plt.savefig('sweep.png')

