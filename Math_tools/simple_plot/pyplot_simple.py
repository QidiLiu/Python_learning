import matplotlib.pyplot as plt
import numpy as np
from phi import phi
from list_linspace import list_linspace
from math import pi

# 自定义定义域 —— 闭集[start, stop]
start = -2
stop = 2

x = list_linspace(start, stop, 10000)
y = []

for i in x:
    y.append(phi(i))

plt.plot(x, y)
plt.grid(color='r', linestyle='--', linewidth=1,alpha=0.3)
plt.xlabel('x')
plt.ylabel('y')
plt.title('y = f(x)')
plt.show()
