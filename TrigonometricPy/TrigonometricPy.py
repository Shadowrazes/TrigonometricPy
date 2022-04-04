import math, cmath
import matplotlib.pyplot as plt
import numpy as np

class FuncEq:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def A(data, k, n):
    sum = 0
    for i in range(n):
        a = -2j * math.pi * i * k / n
        c = cmath.exp(a)
        sum += data[i].y * c
    return sum

def Y_x(data, T, x, n):
    sum = 0
    for i in range(int(-n / 2) + 1, int(n / 2) + 1):
        a = 2j * math.pi * i * (x - data[0].x) / T
        c = cmath.exp(a)
        sum += A(data, i, n) * c
    return sum / n

def graph(X, Y, descr, figureNum):
    plt.figure(figureNum)
    plt.plot(X, Y, label = descr)
    plt.legend()

data = [FuncEq(0, 0), FuncEq(math.pi / 4, 1), FuncEq(math.pi / 2, 0), FuncEq(3 * math.pi / 4, -1), FuncEq(math.pi, 0)]
T = data[len(data) - 1].x - data[0].x
x =  1
n = len(data) - 1
y = Y_x(data, T, x, n)
print("y(2 * ", x, ") = ",y.real)
print("sin(2 * ", x, ") = ",math.sin(2 * x))

X = np.arange(0, 2 * math.pi, 0.1)
Y = []
sin = []

for i in range(len(X)):
    Y.append(Y_x(data, T, X[i], n).real)
    sin.append(math.sin(2 * X[i]))
    
graph(X, Y, "intrp sin(2x)", 1)
graph(X, sin, "sin(2x)", 2)
plt.show()