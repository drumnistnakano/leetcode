#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for nums_idex in range(len(nums)):
            if nums[nums_idex] not in hash:
                hash[nums[nums_idex]] = 1
            else:
                hash[nums[nums_idex]] += 1
        sorted_hash = sorted(hash.items(), key = lambda x: x[1], reverse = True)

        output = []
        for ki in range(k):
            output.append(sorted_hash[ki][0])
        return output
# @lc code=end

