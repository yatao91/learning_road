# -*- coding: utf-8 -*-
"""快速排序算法Python实现"""
from typing import List


class QuickSort:

    @staticmethod
    def _partition(nums: List[int], p: int, r: int) -> int:
        x = nums[r]
        i = p - 1
        for j in range(r):
            if nums[j] <= x:
                i = i + 1
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp

        tmp = nums[r]
        nums[r] = nums[i + 1]
        nums[i + 1] = tmp

        return i + 1

    def sort(self, nums: List[int], p: int, r: int):
        if p < r:
            q = self._partition(nums, p, r)
            self.sort(nums, p, q - 1)
            self.sort(nums, q + 1, r)


if __name__ == '__main__':
    nums = [1]
    QuickSort().sort(nums, 0, len(nums) - 1)
    print(nums)
