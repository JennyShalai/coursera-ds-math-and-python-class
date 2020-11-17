import math 
import numpy as np
import scipy as scipy
import matplotlib.pyplot as plt
%matplotlib inline

def f(x):
    return np.sin(x/5) * np.exp(x/10) + 5*np.exp(-x/2)

# [1.,4.,10.,15.]
X = [[1, 1, 1, 1], [1, 4, 16, 64], [1, 10, 100, 1000], [1, 15, 225, 3375]]
Y = [f(1.), f(4.), f(10.), f(15.)]
B = scipy.linalg.solve(X, Y)
print(B)

# апроксимация функции полинома второй степени
X0 = np.array([1,8,15])
Y0 = np.array([f(1.),f(8.),f(15.)])
W0 =  np.polyfit(X0, Y0, 2)
print(np.flip(W0))
p0 = np.poly1d(W0)

# апроксимация функции полинома третей степени
X1 = np.array([1,4,10,15])
Y1 = np.array([f(1.),f(4.),f(10.),f(15.)])
W1 =  np.polyfit(X1, Y1, 3)
print(np.flip(W1))
p1 = np.poly1d(W1)

xp = np.linspace(0,16,100)
_ = plt.plot(X1, Y1, '*', xp, f(xp), '-', xp, p0(xp), '--', xp, p1(xp), '.')
plt.show()
