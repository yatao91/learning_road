# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        min_path = []
        cur_idx = 0
        sibling_idx = None

        for l in triangle:
            if sibling_idx is None:
                min_node = l[cur_idx]
                cur_idx = cur_idx
                sibling_idx = cur_idx + 1
                min_path.append(min_node)
            else:
                cur_node = l[cur_idx]
                sibling_node = l[sibling_idx]
                if cur_node <= sibling_node:
                    min_path.append(cur_node)
                    cur_idx = cur_idx
                    sibling_idx = cur_idx + 1
                else:
                    min_path.append(sibling_node)
                    cur_idx = sibling_idx
                    sibling_idx = cur_idx + 1

        return min_path


if __name__ == '__main__':
    triangle = [
        [-1],
        [2, 3],
        [1, -1, -3]
    ]
    result = Solution().minimumTotal(triangle)
    print(result)
