import math, cmath

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
    for i in range(int(-n / 2), int(n / 2) + 1):
        a = 2j * math.pi * i * (x - data[0].x) / T
        c = cmath.exp(a)
        sum += A(data, i, n) * c
    return sum / n

data = [FuncEq(0, 0), FuncEq(math.pi / 2, 1), FuncEq(math.pi, 0), FuncEq(3 * math.pi / 2, -1), FuncEq(2 * math.pi, 0)]
T = (len(data) - 1) * math.pi / 2 
x =  math.pi / 4
n = len(data) - 1
y = Y_x(data, T, x, n)
print("y(", x, ") = ",y.real)
print("sin(", x, ") = ",math.sin(x))