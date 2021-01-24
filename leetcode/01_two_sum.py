# -*- coding: utf-8 -*-

"""
Given an array of integers, return indices of the two numbers
such that they add up to hardware specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    # 1.暴力法
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]
        return "No two sum solution"

    # 2.两遍哈希表法
    def twoSumHash_2(self, nums, target):
        hash_map = {}
        for index, value in enumerate(nums):
            hash_map[value] = index
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map and hash_map[complement] != i:
                return [i, hash_map[complement]]
        return "No two sum solution"

    # 3.一遍哈希表法
    def twoSumHash_1(self, nums, target):
        hash_map = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in hash_map:
                return [hash_map[complement], index]
            hash_map[value] = index
        return "No two sum solution"


if __name__ == '__main__':
    s = Solution()
    result = s.twoSumHash_1(nums=[2, 7, 11, 15], target=9)
    print(result)
