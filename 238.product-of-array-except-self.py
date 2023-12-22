#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output_array = [1] * len(nums)

        for i in range(1, len(nums)):
            output_array[i] = output_array[i-1] * nums[i-1]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output_array[i] *= postfix
            postfix *= nums[i]
        return output_array
# @lc code=end

