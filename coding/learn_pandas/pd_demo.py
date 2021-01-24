# -*- coding: UTF-8 -*-
import pandas as pd
import numpy as np
from pandas import Series, DataFrame

x1 = Series([1, 2, 3, 4])
x2 = Series(data=[1, 2, 3, 4], index=['hardware', 'b', 'c', 'd'])

print(x1)
print(x2)

d = {'hardware': 1, 'b': 2, 'c': 3, 'd': 4}
x3 = Series(d)
print(x3)

data = {'Chinese': [66, 95, 93, 90, 80],
        'English': [65, 85, 92, 88, 90],
        'Math': [30, 98, 96, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data,
                index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'],
                columns=['English', 'Math', 'Chinese'])
print(df1)
print(df2)

# 删除dataframe中不必要的行或列
# df2 = df2.drop(columns=['Chinese'])
# df2 = df2.drop(index=['ZhangFei'])
# print(df2)

# 重命名列明
# df2.rename(columns={'Chinese': 'YuWen', 'English': 'YingYu'}, inplace=True)
# print(df2)

# 去重复的值(行)
df2 = df2.drop_duplicates()

# 更改数据格式
df2['Chinese'].astype('str')
df2['Chinese'].astype(np.int64)

# 数据间的空格
# df2['Chinese'] = df2['Chinese'].map(str.strip)
# df2['Chinese'] = df2['Chinese'].map(str.lstrip)
# df2['Chinese'] = df2['Chinese'].map(str.rstrip)
# df2['Chinese'] = df2['Chinese'].str.strip('$')

# 大小写转换
df2.columns = df2.columns.str.upper()
df2.columns = df2.columns.str.lower()
df2.columns = df2.columns.str.title()

# 查找空值 df.isnull() df.isnull().any()

# 使用apply函数对数据进行清洗 df['name'] = df['name'].apply(str.upper)

# 统计
df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'hardware', 'b', 'c'],
                 'data1': range(5)})
print(df1.describe())

# 数据表合并
df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'hardware', 'b', 'c'],
                 'data1': range(5)})
df2 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'A', 'B', 'C'],
                 'data2': range(5)})

# 1.基于指定列进行连接
df3 = pd.merge(df1, df2, on='name')
print(df3)

# 2.inner内连接
df3 = pd.merge(df1, df2, how='inner')
print(df3)

# 3.left左连接
df3 = pd.merge(df1, df2, how='left')
print(df3)

# 4.right右连接
df3 = pd.merge(df1, df2, how='right')
print(df3)

# 5.outer外连接
df3 = pd.merge(df1, df2, how='outer')
print(df3)
