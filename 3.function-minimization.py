import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def f(x):
    return np.sin(x/5) * np.exp(x/10) + 5*np.exp(-x/2)

# отрисовать график функции для наглядности
xp = np.linspace(0,30,100)
_ = plt.plot( xp, f(xp), '-')
plt.show()

# task 1
task1_1 = minimize(f, 5)
print(task1_1.fun)

task1_2 = minimize(f, 2, method = 'BFGS')
print(task1_2.fun)

task1_3 = minimize(f, 30, method = 'BFGS')
print(task1_3.fun)

# task 2
from scipy.optimize import differential_evolution

bounds = [(1, 30)]
task2_1 = differential_evolution(f, bounds)
print(task2_1)

# task 3
def f2(x): 
    return int(np.sin(x/5) * np.exp(x/10) + 5*np.exp(-x/2))

task3_1 = minimize(f2, 30, method = 'BFGS')
print(task3_1.fun)

bounds = [(1,30)]
task3_2 = differential_evolution(f2, bounds)
print(task3_2.fun)
