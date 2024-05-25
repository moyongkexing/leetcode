#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # time: O(n), space: O(n)
        longest_streak_count, nums_set = 0, set(nums)
        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_streak_count = 1
                while current_num + 1 in nums_set:
                    current_streak_count += 1
                    current_num += 1

                longest_streak_count = max(longest_streak_count, current_streak_count)
        return longest_streak_count


# @lc code=end
