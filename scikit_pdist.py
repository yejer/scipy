from scipy import spatial
import matplotlib.pyplot as plt
import numpy as np

a = np.array([[2, 0], [0, 3], [1, 0], [2, 3]])
b = np.array([[0, 0], [1, 3], [1, 2], [2, 4]])

Y = spatial.distance.pdist(a, 'cityblock')
R = spatial.distance.cdist(a, b, 'cityblock')

print Y
print R
print np.argmin(Y)


plt.figure()
plt.grid(b=True, which='major', axis='both')
plt.plot(*zip(*a), marker = 'o', color = 'r', ls = '')
plt.plot(*zip(*b), marker = 'o', color = 'b', ls = '')
plt.show()