import matplotlib.pyplot as plt
import numpy as np

fig_2 = plt.figure()
fig_2, ax_lst = plt.subplots(2, 2)
fig_2.suptitle('Title')
ax_1 = ax_lst[0, 0]
ax_2 = ax_lst[0, 1]
ax_3 = ax_lst[1, 0]
ax_4 = ax_lst[1, 1]

x = np.linspace(0, 2, 100)

ax_1.plot(x, x, label='linear')
ax_1.plot(x, x**2, label='quadratic')
ax_1.plot(x, x**3, label='cubic')
ax_2.plot(x, x)
ax_3.plot(x, x**2)
ax_4.plot(x, x**3)

ax_1.grid(color='r', linestyle='--', linewidth=1,alpha=0.3)

ax_1.set_xlabel('x - ax_1')
ax_1.set_ylabel('y - ax_1')
ax_2.set_xlabel('x - ax_2')
ax_2.set_ylabel('y - ax_2')
ax_3.set_xlabel('x - ax_3')
ax_3.set_ylabel('y - ax_3')
ax_4.set_xlabel('x - ax_4')
ax_4.set_ylabel('y - ax_4')

ax_1.set_title("All in One")
ax_2.set_title("Linear")
ax_3.set_title("Quadratic")
ax_4.set_title("Cubic")

ax_1.legend()

plt.show()