# -*- coding: utf-8 -*-
"""
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
        """
        思路:每轮循环,判断是否括号是否成对出现,出现则替换为空.合法括号内部总会有成对出现括号.
        时间复杂度: O(n),n为内部括号对数
        空间复杂度: 3O(n),n为字符串长度
        """
        while "{}" in s or "()" in s or "[]" in s:
            s = s.replace("{}", "")
            s = s.replace("[]", "")
            s = s.replace("()", "")
        return s == ""

    def isValid2(self, s: str) -> bool:
        """
        思路:借助栈的形式,遍历字符串进行入栈操作,每次入栈时,判断当前字符是否为右括号,如果是,则对比栈顶是否为对应的左括号,是则pop,否则push
        当第一个入栈的为右括号,则非合法括号.
        时间复杂度: O(n),遍历所有的字符串中的括号
        空间复杂度: O(n),最坏需要将所有的括号入栈
        """
        if not s:
            return True
        if len(s) & 1:
            return False
        paren_mapping = {")": "(", "]": "[", "}": "{"}
        temp_stack = []
        for char in s:
            if not temp_stack:
                if char in paren_mapping:
                    return False
                else:
                    temp_stack.append(char)
            else:
                if char in paren_mapping:
                    if temp_stack[-1] == paren_mapping[char]:
                        temp_stack.pop()
                    else:
                        return False
                else:
                    temp_stack.append(char)
        if not temp_stack:
            return True
        else:
            return False

    def isValid3(self, s: str) -> bool:
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        stack = ['?']  # 借助哨兵值,避免pop空栈异常
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False  # 提前结束,提升算法效率
        return len(stack) == 1


if __name__ == '__main__':
    string = "[()]"
    print(Solution().isValid3(string))
