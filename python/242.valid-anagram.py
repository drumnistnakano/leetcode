#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = sorted(s)
        tt = sorted(t)

        if(len(ss) != len(tt)):
            return False

        for i in range(len(ss)):
            if(ss[i] != tt[i]):
                return False

        return True
# @lc code=end

