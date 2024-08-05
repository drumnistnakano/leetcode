#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1
        while top <= bot:
            row_mid = (top + bot) // 2
            if target > matrix[row_mid][-1]:
                top = row_mid + 1
            elif target < matrix[row_mid][0]:
                bot = row_mid - 1
            else:
                break
        
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        l, r = 0, COLS - 1
        while l <= r:
            mid_col = (l + r) // 2
            if target > matrix[row][mid_col]:
                l = mid_col + 1
            elif target < matrix[row][mid_col]:
                r = mid_col - 1
            else:
                return True
        return False
# @lc code=end

