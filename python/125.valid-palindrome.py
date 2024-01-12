#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_array = re.findall('[a-zA-Z0-9]', s.lower())
        return str_array == list(reversed(str_array))
# @lc code=end

