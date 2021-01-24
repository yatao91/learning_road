# -*- coding: UTF-8 -*-


class Solution:

    def valid_palindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                result1 = self.is_valid(s, i + 1, j)
                result2 = self.is_valid(s, i, j - 1)

                return any([result1, result2])
            i += 1
            j -= 1
        return True

    @staticmethod
    def is_valid(s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


if __name__ == '__main__':
    solution = Solution()
    string = "abca"
    print(solution.valid_palindrome(string))
