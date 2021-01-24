# -*- coding: UTF-8 -*-
"""
给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。
找到 nums1 中每个元素在 nums2 中的下一个比其大的值。
nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

示例 1:
输入: nums1 = [4,1,2], nums2 = [1,3,4,2].
输出: [-1,3,-1]
解释:
    对于num1中的数字4，你无法在第二个数组中找到下一个更大的数字，因此输出 -1。
    对于num1中的数字1，第二个数组中数字1右边的下一个较大数字是 3。
    对于num1中的数字2，第二个数组中没有下一个更大的数字，因此输出 -1。

示例 2:
输入: nums1 = [2,4], nums2 = [1,2,3,4].
输出: [3,-1]
解释:
    对于 num1 中的数字 2 ，第二个数组中的下一个较大数字是 3 。
    对于 num1 中的数字 4 ，第二个数组中没有下一个更大的数字，因此输出 -1 。

提示：
nums1和nums2中所有元素是唯一的。
nums1和nums2 的数组大小都不超过1000。
"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_dict = {}
        for i, num in enumerate(nums2):
            greater_dict[num] = -1
            for j in range(i+1, len(nums2)):
                if nums2[j] > num:
                    greater_dict[num] = nums2[j]
                    break
        greater_list = []
        for num in nums1:
            greater_list.append(greater_dict[num])
        return greater_list

    def nextGreaterElement2(self, nums1, nums2):
        """
        思路:利用单调栈(辅助栈)存储单调的栈(此处是递减).
        时间复杂度:看似for+while循环为O(n^2),实际push元素n次,而最多会pop一次.
        空间复杂度:O(n),需要使用辅助单调栈且用字典临时存储数组2的答案.
        """
        greater_list = []
        greater_dict = {}
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                greater_dict[stack.pop()] = num
            stack.append(num)
        if stack:
            length = len(stack)
            for i in range(length):
                greater_dict[stack.pop()] = -1
        for num in nums1:
            greater_list.append(greater_dict[num])
        return greater_list
