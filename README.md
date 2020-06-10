# Метод Гаусса  
## Задание:  
Сравнить решение СЛАУ методом Гаусса библиотечной функцией np.linalg.solve со всей реализацией на случайной матрицей с диагональным преобладанием размером 100x100, 200x200 и т.д.
Провести несколько экспериментов, пока время счета меньше 1 сек. Построить графики зависимостей.  
## Как запустить?  
1) Вводим размер матрицы nxn  
2) Вводим матрицу размера nxn в матричном виде  
  
Пример:  
матрица 3x3  
1 2 3  
1 2 3  
1 2 3  
  
3) Вводим столбец f размера n  
## Что выводит программа?  
for n = 100 ||x - x_compare|| = 2.3111108307014155e-16  
for n = 200 ||x - x_compare|| = 2.0158624124883814e-14  
for n = 300 ||x - x_compare|| = 7.773429547796606e-13  
for n = 400 ||x - x_compare|| = 6.884508943663701e-11  
for n = 500 ||x - x_compare|| = 1.6389731531537222e-08  
x - вектор который посчитан методом Гаусса  
x_compare - вектор, который получен в результате использования функции np.linalg.solve  
Программа выводит норму вектора (x - x_compare), чтобы показать как сильно отличаются значения.  
### График  
![alt text](foo.png "graph")​
