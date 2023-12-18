#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}

        for str in strs:
            sort_str = ''.join(sorted(str))
            if sort_str not in hash:
                hash[sort_str] = [str]
            else:
                hash[sort_str].append(str)

        arrayOutput = []
        for index in hash:
            arrayOutput.append(hash[index])

        print(arrayOutput)
        return arrayOutput
# @lc code=end