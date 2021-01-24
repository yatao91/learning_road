# -*- coding: UTF-8 -*-
"""
14. 最长公共前缀
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 hardware-z
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        1.水平扫描法
        思路:先假设第一个字符串为最小公共前缀,然后遍历后面的字符串,逐个得到前缀,前缀为空时终止循环;或遍历到最后一个元素
        时间复杂度:最坏O(S), S为所有字符串字符总和
        空间复杂度:O(1),常量级存储空间
        """
        if strs is None or len(strs) == 0:
            return ""
        i = 1
        common_prefix = strs[0]
        while i < len(strs):
            common_prefix = self.find_longest_common_prefix(common_prefix, strs[i])
            if not common_prefix:
                return ""
            i += 1
        return common_prefix

    def find_longest_common_prefix(self, str1, str2):
        short_length = min(len(str1), len(str2))
        for i in range(short_length):
            if str1[i] != str2[i]:
                return str1[:i]
        return str1[:short_length]

    def longestCommonPrefix2(self, strs):
        """
        2.垂直扫描
        思路:遍历第一个字符串的每个字符,并同时对比后续的对应位置字符,当遍历第一个字符串的某个位置时,位置等于后续
        某字符串长度或某字符串对应位置字符不相等时,则终止遍历;或遍历到结束.避免数组末尾元素最短时,第一种水平扫描法
        依旧遍历到底的原因
        时间复杂度: O(S),最坏为字符串中字符数量的总和.最坏情况与第一种相同,但最好情况下仅需要n*minLen(n为字符串个数)
        空间复杂度: O(1).常数级别的空间复杂度
        """
        if strs is None or len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return strs[0][0:i]
        return strs[0]

    def longestCommonPrefix3(self, strs):
        """
        n个长度为m的相同字符串
        思路:采用分治法
        时间复杂度: O(S),S是所有字符串中字符的总和.T(n)=2*T(n/2) + O(m),化简后为O(S).最好情况下,
        minLen*n次比较.minLen为最短字符串长度
        空间复杂度:O(m*log(n)):内存开支主要是递归过程中的栈空间消耗的.一共进行log(n)次递归,每次需要m的空间返回存储结果.
        """
        if strs is None or len(strs) == 0:
            return ""
        return self.sub_longest_common_prefix(strs, 0, len(strs)-1)

    def sub_longest_common_prefix(self, strs, left, right):
        if left == right:
            return strs[left]
        else:
            mid = (left + right) // 2
            left_prefix = self.sub_longest_common_prefix(strs, left, mid)
            right_prefix = self.sub_longest_common_prefix(strs, mid + 1, right)
            return self.find_longest_common_prefix(left_prefix, right_prefix)


if __name__ == '__main__':
    solution = Solution()
    str_list = ["flower", "flight"]
    result = solution.longestCommonPrefix3(str_list)
    print(result)
