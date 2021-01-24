# -*- coding: utf-8 -*-
"""
58.最后一个单词的长度
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。

示例:
输入: "Hello World"
输出: 5
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list = s.split()
        if not word_list:
            return 0
        return len(word_list[-1])

    def lengthOfLastWord2(self, s):
        """
        思路:从后向前遍历,需考虑判断末尾空格,若末尾为空格,则end尾部需前移.前移到非空格时,置为start,向前遍历直到遇到第一个空格.start-end即
        最后一个单词长度
        时间复杂度:O(n)
        空间复杂度:O(1)
        """
        end = len(s) - 1
        while end >= 0 and s[end] == " ":
            end -= 1
        start = end
        while end >= 0 and s[end] != " ":
            end -= 1
        return start - end


if __name__ == '__main__':
    string = "hello world"
    print(Solution().lengthOfLastWord2(string))
