#!/bin/bash

# 定义变量:变量名和等号之间无空格
your_name="suyatao"

# 使用变量:变量名前＋美元符号即可
echo $your_name
echo ${your_name}  # 花括号可选.加花括号目的:识别变量名边界  推荐给变量名添加花括号

# 使用语句给变量赋值
for file in `ls /etc`

# 重定义变量
your_name="sususu"
echo ${your_name}

your_name="2222"
echo ${your_name}

# 字符串
# 单引号: 字符原样输出;单引号字符串中变量无效;单引号字符串中不能出现单引号
str='string'

# 双引号: 可以有变量;可以出现转移字符
your_name="liqiang"
str="hello \"${your_name}\""

# 拼接字符串
your_name='suqiang'
greeting="hello \"${your_name}\""
greeting_1="hello ${your_name}"

echo $greeting $greeting_1

# 获取字符串长度
string="abcd"
echo ${#string}  # 输出4

# 提取子字符串
string="alibaba is a great company"
echo ${string:1:4}  # 输出liba

# 查找子字符串
string="alibaba is a great company"
echo `expr index "$string" is` # 输出: 3
