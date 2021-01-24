# -*- coding: UTF-8 -*-


class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        special_map = {
            "I": {"V", "X"},
            "X": {"L", "C"},
            "C": {"D", "M"}
        }
        num = 0
        for index, c in enumerate(s):
            if c in special_map:
                next_index = index + 1
                if next_index == len(s):
                    num += roman_map[c]
                else:
                    if s[next_index] in special_map[c]:
                        num -= roman_map[c]
                    else:
                        num += roman_map[c]
            else:
                num += roman_map[c]
        return num

    def romanToInt2(self, s: str) -> int:
        roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        for i in range(len(s)):
            if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i+1]]:
                num -= roman_map[s[i]]
            else:
                num += roman_map[s[i]]
        return num


if __name__ == '__main__':
    solution = Solution()
    char = "VX"
    result = solution.romanToInt(char)
    print(result)
