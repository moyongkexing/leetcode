#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Brute Force
        # time: O(n^2), space: O(1)
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # optimized
        # time: O(n), space: O(n)
        table = {}
        for ind, value in enumerate(nums):
            if value in table:
                return table[value], ind
            table[target - value] = ind


# @lc code=end
