# -*- coding: UTF-8 -*-
import numpy as np

x1 = np.arange(1, 11, 2)
x2 = np.linspace(1, 9, 5)

print(np.add(x1, x2))  # 加
print(np.subtract(x1, x2))  # 减
print(np.multiply(x1, x2))  # 乘
print(np.divide(x1, x2))  # 除
print(np.power(x1, x2))  # 求n次方
print(np.remainder(x1, x2))  # 取余数
