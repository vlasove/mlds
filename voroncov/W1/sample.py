"""
    Немного про работу с numpy
"""
import numpy as np 

# Генерация случ матрицы
# loc - среднее знач
# scale - std
# size(a,b) - a -колво строк, b - стобцов
X = np.random.normal(loc=1, scale=10, size=(1000,50))
#print(X)

# Нормировка матрицы
m = np.mean(X, axis=0)
std = np.std(X, axis=0)

X_norm = (X - m) / std 

Z = np.array([[4, 5, 0], 
             [1, 9, 3],              
             [5, 1, 1],
             [3, 3, 3], 
             [9, 9, 9], 
             [4, 7, 1]])
r = np.sum(Z, axis=1)
print(np.nonzero(r > 10))


# Соединение двух матриц в одну
A = np.eye(3)
B = np.eye(3)

AB = np.vstack((A,B))
A_B = np.hstack((A,B))
print(AB)
print(A_B)