#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start


from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hash = {}
        # for i in range(len(nums)):
        #     if nums[i] in hash:
        #         return True
        #     hash[nums[i]] = 1
        # return False

        # hset = set()
        # for idx in nums:
        #     if idx in hset:
        #         return True
        #     else:
        #         hset.add(idx)

        # one-line
        # If there is a duplicate element then set function will give a list
        # which less has length less than the actual list.
        return len(set(nums)) != len(nums)


# @lc code=end
