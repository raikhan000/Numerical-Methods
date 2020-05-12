from math import sqrt
import numpy as np
print('Введите размер матрицы nxn')
n = int(input())
print('Введите матрицу')
l = [[float(j) for j in input().split()]for i in range(n)]
a = np.array(l)

L = [[0.0]* n for i in range(n)]
L = np.array(L)
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


print(L)
print(L.transpose())
