#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        result = r

        while l <= r:
            k = (l + r) // 2
            total_time = 0

            for p in piles:
                total_time += math.ceil(p / k)

            if total_time <= h:
                result = k
                r = k - 1
            else:
                l = k + 1
        return result
# @lc code=end

