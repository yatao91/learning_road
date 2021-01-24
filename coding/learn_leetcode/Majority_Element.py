# -*- coding: utf-8 -*-
from typing import List


class Solution:

    def majorityElement(self, nums: List[int]) -> int:

        cur = None
        count = 0

        for num in nums:

            # 将数组第一个值赋值给当前值,出现次数赋值1
            if cur is None:
                cur = num
                count = 1
                continue

            # 判断出现元素是否和候选元素相同, 相同则加1,不同则减1
            if cur == num:
                count += 1
            else:
                count -= 1

                # 如果count为0,则代表子数组无候选元素,将cur指向当前元素,赋值count为1,进行后续投票
                if count == 0:
                    cur = num
                    count = 1

        # 如果最终计数小于等于0,则无候选元素,返回0
        if count <= 0:
            return 0
        # 否则, 验证此候选元素是否确定大于数组一半长度
        else:
            count = 0
            for num in nums:
                if cur == num:
                    count += 1

            if count > len(nums) / 2:
                return cur
            else:
                return 0


if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]

    ret = Solution().majorityElement(nums)
    print(ret)
