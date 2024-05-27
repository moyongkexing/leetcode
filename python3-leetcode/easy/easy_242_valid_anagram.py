#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#


# @lc code=start


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using hash table
        # count = defaultdict(int)
        # for x in s:
        #     count[x] += 1
        # for x in t:
        #     count[x] -= 1

        # for val in count.values():
        #     if val != 0:
        #         return False
        # return True

        # one-line
        # return collections.Counter(s) == collections.Counter(t)

        # using hash table with array
        count = [0] * 26
        for x in s:
            count[ord(x) - ord("a")] += 1
        for x in t:
            count[ord(x) - ord("a")] -= 1
        for val in count:
            if val != 0:
                return False
        return True

        # using sorting
        # time: O(logN), space: ?
        # return sorted(s) == sorted(t)

        # using set
        # if len(s) != len(t):
        #     return False

        # for val in set(s):
        #     if s.count(val) != t.count(val):
        #         return False
        # return True


# @lc code=end
