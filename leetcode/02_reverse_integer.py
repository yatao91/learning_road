# -*- coding: utf-8 -*-

"""
Given hardware 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def reverse(self, x: int) -> int:
        sign = False
        if x < 0:
            sign = True

        x = abs(x)

        x = str(x)

        chars = []
        for c in x:
            chars.append(c)

        chars.reverse()

        y = ''.join(chars)

        y.split('0')

        y = int(y)

        if sign:
            if y > 2 ** 31:
                y = 0
            else:
                y = -y
        else:
            if y > 2 ** 31 - 1:
                y = 0
            else:
                y = y
        return y

    def reverse_2(self, x):
        rev = 0

        if x > 0:
            flag = True
        elif x < 0:
            flag = False
        else:
            return rev

        while x != 0:
            x = abs(x)
            pop = x % 10
            x = x // 10

            if flag:
                if rev > 2**31 // 10 or (rev == 2**31 // 10 and pop > 7):
                    return 0
            else:
                if rev > 2**31 // 10 or (rev == 2**31 // 10 and pop > 8):
                    return 0
            rev = rev * 10 + pop

        if flag:
            return rev
        return -rev


if __name__ == '__main__':
    s = Solution()
    ret = s.reverse_2(-765761230)
    print(ret)
