from scipy import spatial
import numpy as np


x, y = np.mgrid[1:10, 2:10]
# tree = spatial.KDTree(list(zip(x.ravel(), y.ravel())))
points = zip(x.ravel(), y.ravel())
tree = spatial.KDTree(points)
print tree.data


# This returns a list like ('return ', [4L])
output = tree.query_ball_point([6, 2], 1)
print output
# print ("return " ,  tree.query_ball_point([6, 2], 2))

# put the index of list "4"  and it will show the nearest points
for i in output:
    print tree.data[i]


