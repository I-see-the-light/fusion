import numpy as np
p1 = [1, 3, 6, 1]
p2 = [2, 4, 8, 8]
p3 = [-1, 5, 4, 0]
mat = np.stack((p1, p2, p3), axis=0)
print(np.cov(mat))
