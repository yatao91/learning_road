# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums1:
            return []
        if not nums2:
            return []

        l1 = len(nums1)
        l2 = len(nums2)
        result = []
        hash_num = {}
        if l1 < l2:
            for num in nums1:
                if num in hash_num:
                    t = hash_num[num]
                    hash_num[num] = t + 1
                else:
                    hash_num[num] = 1
            for num in nums2:
                if num in hash_num:
                    t = hash_num[num]
                    if t > 0:
                        result.append(num)
                        hash_num[num] = t - 1
                    else:
                        continue
        else:
            for num in nums2:
                if num in hash_num:
                    t = hash_num[num]
                    hash_num[num] = t + 1
                else:
                    hash_num[num] = 1
            for num in nums1:
                if num in hash_num:
                    t = hash_num[num]
                    if t > 0:
                        result.append(num)
                        hash_num[num] = t - 1
                    else:
                        continue
        return result


if __name__ == '__main__':
    s = Solution()
    l1 = [1, 2, 2, 1]
    l2 = [2]

    result = s.intersect(nums1=l1, nums2=l2)
    print(result)
