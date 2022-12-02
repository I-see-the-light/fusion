import numpy as np
p1 = [1, 0, -1, 1]
p2 = [3, 4, 2, -1]
p3 = [-1, 2, 2, 0]
mat = np.stack((p1, p2, p3), axis=1)
print(np.cov(mat))