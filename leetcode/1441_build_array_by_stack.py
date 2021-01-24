# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        operation_array = []
        length = len(target)
        index = 0
        for i in range(1, n+1):
            if target[index] == i:
                operation_array.append("Push")
                index += 1
            else:
                operation_array.append("Push")
                operation_array.append("Pop")
            if index >= length:
                break
        return operation_array


if __name__ == '__main__':
    solution = Solution()
    target_array, n = [1, 3], 3
    result = solution.buildArray(target_array, n)
    print(result)
