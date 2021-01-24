# -*- coding: UTF-8 -*-


class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            # 判断是否是字母或者数字
            if not self.is_num_or_alpha(s[i]):
                i += 1
                continue
            if not self.is_num_or_alpha(s[j]):
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

    @staticmethod
    def is_num_or_alpha(char: str) -> bool:
        if char.isalnum() or char.isalpha():
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    string = "A man, hardware plan, hardware canal: Panama"
    print(solution.isPalindrome(string))
