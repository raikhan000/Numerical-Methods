import time
from math import sqrt
import numpy as np
import matplotlib.pyplot as plt
def Kholetskiy(a,n):
	L = np.zeros((n,n))
	temp1 = temp2 = 0

	L[0][0] = sqrt(a[0][0])
	for i in range(1,n):
		L[i][0] = a[i][0]/L[0][0]

	for i in range(1, n):
		for j in range(1, n):
			temp1 = 0
			temp2 = 0

			if i > j:
				for k in range(j):
					temp1 += L[i][k]*L[j][k]
				L[i][j] = (a[i][j] - temp1) / L[j][j]
			if i == j:
				for k in range(i):
					temp2 += L[i][k]*L[i][k]
				L[i][i] = sqrt(a[i][i] - temp2)
	return L     

k = 5
kh_time = np.zeros(k)
library_time = np.zeros(k)
for i in range(1,k+1):
	n = i*100
	print(n)
	a = np.random.rand(n,n)
	a = np.tril(a)
	for m in range(n):
		for k in range(n):
			if k > m:
				a[m][k] = a[k][m]

	s = np.sum(np.abs(a), axis = 1)
	for j in range(n):
		a[j][j] = a[j][j] + s[j]


	t1 = time.time()
	L = Kholetskiy(a,n)
	det = np.linalg.slogdet(L)
	print("Определитель L:",det)
	t2 = time.time() - t1
	kh_time[i-1] = t2

	t1 = time.time()
	L_compare = np.linalg.cholesky(a)
	det_compare = np.linalg.slogdet(L_compare)
	print("Определитель L_compare",det_compare)

	t2 = time.time() - t1
	library_time[i-1] = t2

plt.plot(kh_time)
plt.plot(library_time)
plt.savefig('foo1.png')
