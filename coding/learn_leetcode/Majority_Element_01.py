# -*- coding: utf-8 -*-
from typing import List


class Solution:

    def majorityElement(self, nums: List[int]) -> int:

        d = {}
        for num in nums:

            if d.get(num):
                d[num] += 1
            else:
                d[num] = 1

        for key, value in d.items():

            if value > len(nums) / 2:
                return key
        else:
            return 0


if __name__ == '__main__':
    nums = [2, 2, 1]

    ret = Solution().majorityElement(nums)
    print(ret)
