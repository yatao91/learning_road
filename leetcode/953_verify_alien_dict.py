# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pass


if __name__ == '__main__':
    solution = Solution()
    words = ["hello", "leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    result = solution.isAlienSorted(words=words, order=order)
    print(result)
