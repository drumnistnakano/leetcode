#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                if (board[i][j] in rows[i]
                    or board[i][j] in cols[j]
                    or board[i][j] in squares[(i // 3, j // 3)]):
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(i // 3, j //3)].add(board[i][j])

        return True
# @lc code=end

