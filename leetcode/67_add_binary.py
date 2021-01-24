# -*- coding: utf-8 -*-
"""
67.二进制求和
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

示例 1:
输入: hardware = "11", b = "1"
输出: "100"
示例 2:

输入: hardware = "1010", b = "1011"
输出: "10101"
 
提示：
每个字符串仅由字符 '0' 或 '1' 组成。
1 <= hardware.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。
"""


class Solution:

    def addBinary(self, a: str, b: str) -> str:
        """
        思路:python内置函数,转换为十进制相加,将和转换为二进制
        时间复杂度:O(M+N)
        """
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary2(self, a, b):
        return '{0:b}'.format(int(a, 2) + int(b, 2))

    def addBinary3(self, a, b):
        """
        思路:逐位计算.借助carry进位制.a的最低位为1,则carry加1;b的最低位为1则carry加1.将carry最低位作为answer最低位的值.最高位移向下一位
        重复直到a和b的每一位计算完毕.最后carry最高位不为0,则添加到计算结果末尾.反转拼接即可.
        时间复杂度:O(MAX(M,N)),a和b最长长度决定
        空间复杂度:O(MAX(M,N)),存储结果
        """
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)

        carry = 0
        answer = []
        for i in range(n-1, -1, -1):
            if a[i] == "1":
                carry += 1
            if b[i] == "1":
                carry += 1

            if carry % 2 == 1:
                answer.append("1")
            else:
                answer.append("0")
            carry //= 2

        if carry == 1:
            answer.append("1")
        answer.reverse()
        return "".join(answer)

    def addBinary4(self, a, b):
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]


if __name__ == '__main__':
    a = "111"
    b = "1"
    print(Solution().addBinary4(a, b))
