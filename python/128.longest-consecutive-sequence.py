#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest_count = 0

        for num in nums:
            if num - 1 not in set_nums:
                length_count = 1
                while num + length_count in set_nums:
                    length_count += 1
                longest_count = max(length_count, longest_count)

        
        return longest_count
# @lc code=end

