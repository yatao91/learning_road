# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)

        # 1.数组为空
        if length == 0:
            return 0

        # 2.数组非空
        for index, num in enumerate(nums):
            if target == num:
                return index
            elif target > num:
                if index + 1 == length:
                    return index + 1
                if target < nums[index + 1]:
                    return index + 1
                if target > nums[index + 1]:
                    continue
            else:
                return index

    def searchInsert2(self, nums, target):
        """
        二分查找
        时间复杂度:O(log(n))
        空间复杂度:O(1)
        :param nums:
        :param target:
        :return:
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    print(Solution().searchInsert2(nums, 0))
