#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        Map = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []

        for i in s:
            if i not in Map:
                stack.append(i)
                continue
            if not stack or stack[-1] != Map[i]:
                return False
            stack.pop()

        return not stack
# @lc code=end

