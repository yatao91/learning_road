# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def merge_01(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        方法一:先将数据合并到nums1中,然后对nums进行排序
        时间复杂度:O((m+n)log(m+n))
        空间复杂度:O(1)
        """
        nums1[:] = sorted(nums1[:m] + nums2)

    def merge_02(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        方法二:先将nums1待合并的数据拷贝出去,然后使用从前到后双指针法比较两数组元素逐个放入原nums1数组中
        时间复杂度:O(m+n)
        空间复杂度:O(m)
        """
        # 1.获取nums1数组拷贝并将原nums1置空
        nums1_copy = nums1[:m]
        nums1[:] = []

        # 2.初始化nums1和nums2指针
        p1 = 0
        p2 = 0

        # 3.仅当两数组指针均未到末尾时,进行比较并将较小值放入nums1数组,对应指针后移一位
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        # 4.处理两数组中未进行比较的数值,直接添加到nums1数组末尾
        if p1 < m:
            nums1.extend(nums1_copy[p1:])
        if p2 < n:
            nums1.extend(nums2[p2:])

    def merge_03(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        方法三:使用从后向前双指针法进行比较,将大值从后到前放入nums1数组中,不需要额外空间
        时间复杂度:O(m+n)
        空间复杂度:O(1)
        """
        # 1.初始化三个指针
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1

        # 2.比较元素大小,大的放入nums1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1

        # 3.将nums2中遗留的元素添加到nums1中(即使nums2已为空也进行此操作)
        nums1[:p2+1] = nums2[:p2+1]


if __name__ == '__main__':
    array_01 = [1, 2, 3, 0, 0, 0]
    array_02 = [2, 5, 6]

    Solution().merge_03(nums1=array_01, m=3, nums2=array_02, n=3)
    print(array_01)
