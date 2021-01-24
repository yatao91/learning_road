# -*- coding: UTF-8 -*-
"""
有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        paren = {"(": ")", "[": "]", "{": "}"}
        if not s or len(s) & 1 == 1:
            return True
        half_len = len(s) // 2
        for index in range(half_len):
            if paren[s[index]] != s[len(s) - index - 1]:
                return False
        return True


if __name__ == '__main__':
    string = "()"
    print(Solution().isValid(string))
