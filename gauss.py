import numpy as np
import time
import matplotlib.pyplot as plt
def Gauss(a,f,n):
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
    return x

k = 5
gauss_time = np.zeros(k)
library_time = np.zeros(k)
for i in range(1,k+1):
  n = i*100
  a = np.random.rand(n,n)
  f = np.random.rand(n)
  s = np.sum(np.abs(a), axis = 1)

  for m in range(n):
    a[m][m] = a[m][m] + s[m]

  t1 = time.time()
  x = Gauss(a,f,n)
  t2 = time.time() - t1
  gauss_time[i-1] = t2

  t1 = time.time()
  x_compare = np.linalg.solve(a,f)
  t2 = time.time() - t1
  library_time[i-1] = t2

  print('for n =',n,'||x - x_compare|| = ', np.linalg.norm(x_compare - x))

plt.plot(gauss_time)
plt.plot(library_time)
plt.savefig('foo.png')
