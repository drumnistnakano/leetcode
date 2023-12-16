#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # val -> index
        hash = {}

        for index, value in enumerate(nums):
            diffValue = target - value
            if diffValue in hash:
                return [hash[diffValue], index]
            hash[value] = index
# @lc code=end

