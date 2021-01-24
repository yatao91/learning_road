# -*- coding: UTF-8 -*-
import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# 统计数组最大值/最小值
print(np.amin(a))
print(np.amin(a, 0))
print(np.amin(a, 1))
print(np.amax(a))
print(np.amax(a, 0))
print(np.amax(a, 1))

# 统计最大值与最小值之差
print(np.ptp(a))
print(np.ptp(a, 0))
print(np.ptp(a, 1))

# 统计数组的百分位数
print(np.percentile(a, 50))
print(np.percentile(a, 50, axis=0))
print(np.percentile(a, 50, axis=1))

# 统计中位数/平均数
print(np.median(a))
print(np.median(a, axis=0))
print(np.median(a, axis=1))
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))

# 统计加权平均值
b = np.array([1, 2, 3, 4])
wts = np.array([1, 2, 3, 4])
print(np.average(b))
print(np.average(b, weights=wts))

# 统计标准差/方差
print(np.std(b))
print(np.var(b))
