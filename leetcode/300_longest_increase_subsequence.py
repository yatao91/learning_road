# -*- coding: utf-8 -*-
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        f = [1 for _ in range(n)]

        for x in range(n):
            for p in range(x):
                if nums[x] > nums[p]:
                    f[x] = max(f[x], f[p] + 1)

        ans = 0
        for x in range(n):
            ans = max(ans, f[x])

        return ans

    def lengthOfLIS2(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)


if __name__ == '__main__':
    l = []
    print(Solution().lengthOfLIS2(nums=l))
