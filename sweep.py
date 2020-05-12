import numpy as np
print('Введите размер матрицы nxn')
n = int(input())
print('Введите вектор а')
a = [int(i) for i in input().split()]
print('Введите вектор b')
b = [int(i) for i in input().split()]
print('Введите вектор c')
c = [int(i) for i in input().split()]
A = np.zeros((n,n))

for i in range(n):
	for j in range(n):
		if i == j:
			A[i][i] = b[i]
			if j - 1 >=0:
				A[i][j-1] = a[j]
			if j + 1 < n:
				A[i][j + 1] = c[j]
print(A)
print('Введите вектор свободных членов')
f = [int(i) for i in input().split()]
x = [0] * n
delta = [0] * n
lyambda = [0] * n

delta[0] = -A[0][1]/A[0][0]
lyambda[0] = f[0]/A[0][0]

for i in range(1, n - 1):
	d = 0
	d = A[i][i] + (A[i][i-1]*delta[i-1])
	delta[i] = -A[i][i+1]/ d
	lyambda[i] = (f[i] - A[i][i-1]*lyambda[i-1])/d

delta[n-1] = 0
lyambda[n-1] = (f[n-1] - A[n-1][n-2]*lyambda[n-2])/(A[n-1][n-1] + (A[n-1][n-2]*delta[n-2]))

x[n-1] = lyambda[n-1];
for i in range(n - 2, -1, -1):
	x[i] = delta[i] * x[i+1] + lyambda[i];

print(x)

