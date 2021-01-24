# -*- coding: UTF-8 -*-
import numpy as np

a = np.array([[4, 3, 2], [2, 4, 1]])

print(np.sort(a))
print(np.sort(a, axis=None))
print(np.sort(a, axis=0))
print(np.sort(a, axis=1))
