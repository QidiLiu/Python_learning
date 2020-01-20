# Precision, Recall 和 F1值之间的关系
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

any_precision = np.linspace(0.01, 1, 100)
any_recall = np.linspace(0.01, 1, 100)
any_precision, any_recall = np.meshgrid(any_precision, any_recall)

any_f1_score = 2*any_precision*any_recall/(any_precision+any_recall)

ax.plot_surface(any_precision, any_recall, any_f1_score)  #这里传入x, y, z的值

plt.xlabel('precision')
plt.ylabel('recall')
plt.title('f1 score')

plt.show()