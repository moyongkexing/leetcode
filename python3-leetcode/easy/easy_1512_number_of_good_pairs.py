#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#


# @lc code=start
import math
import collections
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # time: O(n), space: O(n)
        return sum([math.comb(n, 2) for n in collections.Counter(nums).values()])


# @lc code=end
