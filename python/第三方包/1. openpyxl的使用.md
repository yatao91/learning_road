## openpyxl的使用中遇到的问题

###### 1. openpyxl读取速度比xlrd慢了很多

因为xlrd仅用于读取excel内容,但openpyxl是对excel进行读写,当直接进行`load_workbook(filename)`时, 因目的为读写,则读取速度会很慢. 

但是当openpyxl只用于读取excel时,可以设定为只读:

`wb = load_workbook(filename, read_only=True )`

速度明显提升了很多,并且比xlrd稍微快那么一丢丢.

测试代码:

```python
from openpyxl import load_workbook
import xlrd
import time

xlsPath = "/home/vagrant/dev/projects/biplatform/project_test/excel_test.xlsx"

t0 = time.time()
wb1 = load_workbook("/home/vagrant/dev/projects/biplatform/project_test/excel_test.xlsx", read_only=True)
t1 = time.time()
print('openpyxl所用时间:', str(t1-t0))

t2 = time.time()
wb2 = xlrd.open_workbook(xlsPath)
t3 = time.time()
print('xlrd所用时间:', str(t3-t2))
```

测试结果:

```
openpyxl所用时间: 3.5786168575286865
xlrd所用时间: 4.03287410736084
```

###### 2. xlrd读取表格特点

**Excel常用文件格式区别**

- XLS: Excel 2003版本之前使用的文件格式，二进制的文件保存方式。xls文件支持的最大行数是65536行。xlsx支持的最大行数是1048576行。xls支持的的最大列数是256列，xlsx是16384列，这个是行数和列数的限制不是来自Excel的版本而是文件类型的版本。
- XLSX: XLSX其实一个ZIP文件，也就是如果你把文件名的XLSX改成zip，然后是可以用解压缩软件直接打开这个zip文件的，你打开它看到话，会可以看到里面有很多的xml文件。

**不适用xlrd原因:**

1. xlrd对xlsx支持有限, xls格式行数限制问题,导致无法读取大文件.

###### 3. openpyxl读取file_like文件对象

当适用openpyxl读取从云服务器上拉取的文件时, 需要适用BytesIO进行转换成bytes类型然后才可适用openpyxl读取.

`self.book = load_workbook(BytesIO(file_content), read_only=True)`

