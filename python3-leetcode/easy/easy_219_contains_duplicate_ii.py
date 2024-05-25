#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#


# @lc code=start
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Brute Force
        # for i in range(len(nums)):
        #     # The index corresponding to the stop value passed to range function
        #     # is not reached during the loop.
        #     # time: O(n^2), space: O(1)
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True
        # return False

        # optimized
        # time: O(n), space: O(n)
        # hash = {}
        # for i in range(len(nums)):
        #     if nums[i] in hash and abs(hash[nums[i]] - i) <= k:
        #         return True
        #     hash[nums[i]] = i
        # return False

        # using enumerate function
        # time: O(n), space: O(n)
        hash = {}
        for i, v in enumerate(nums):
            if v in hash and i - hash[v] <= k:
                return True
            hash[v] = i
        return False


# @lc code=end
