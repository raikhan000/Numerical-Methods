import numpy as np
print('Введите размер матрицы nxn')
n = int(input())
print('Введите матрицу')
l = [[int(j) for j in input().split()]for i in range(n)]
a = np.array(l)
print('Введите столбец')
f = [int(i) for i in input().split()]
for k in range(n):
	for j in range (k+1, n):
		a[k][j] = a[k][j] / a[k][k]
	for i in range(k+1, n):
		for j in range(k+1, n):
			a[i][j] = a[i][j] - a[i][k] * a[k][j]
		f[i] = f[i] - a[i][k] * f[k]
		a[i][k] = 0
x = [0]*n
for i in range(n - 1,-1, -1):
	s = 0;
	for j in range (i, n):
		s = s + a[i][j] * x[j]
	x[i] = (f[i] - s) / a[i][i]
print('Ответ:')
print(x)

		#M = a[j][k] / a[k][k]
                #for i in range(k , n):
                 #       a[j][i] -= M * a[k][i]
                #f[j] -= M * f[k]
