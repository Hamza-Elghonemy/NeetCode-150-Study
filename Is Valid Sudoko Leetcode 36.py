# Is Valid Sudoko Leetcode 36
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        n = 9
        rows = [set() for _ in range(n)] # create a set for each row
        cols = [set() for _ in range(n)] # create a set for each column
        boxes = [set() for _ in range(n)] # create a set for each 3x3 box
        for r in range(n): 
            for c in range(n):
                val = board[r][c]
                if val == '.':
                    continue
                if val in rows[r] or val in cols[c]:
                    return False
                rows[r].add(val) 
                cols[c].add(val)
                indx = (r//3) * 3 + c // 3
                if val in boxes[indx]:
                    return False
                boxes[indx].add(val)
        return True

# Time complexity: O(1) for fixed size 9x9 board O(n) for n x n board
# Space complexity: O(1) for fixed size 9x9 board O(3n) for n x n board

# Test cases
s = Solution()
print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."],
                        ["6",".",".","1","9","5",".",".","."],
                        [".","9","8",".",".",".",".","6","."],
                        ["8",".",".",".","6",".",".",".","3"],
                        ["4",".",".","8",".","3",".",".","1"],
                        ["7",".",".",".","2",".",".",".","6"],
                        [".","6",".",".",".",".","2","8","."],
                        [".",".",".","4","1","9",".",".","5"],
                        [".",".",".",".","8",".",".","7","9"]])) # True
print(s.isValidSudoku([["8","3",".",".","7",".",".",".","."],
                        ["6",".",".","1","9","5",".",".","."],
                        [".","9","8",".",".",".",".","6","."],
                        ["8",".",".",".","6",".",".",".","3"],
                        ["4",".",".","8",".","3",".",".","1"],
                        ["7",".",".",".","2",".",".",".","6"],
                        [".","6",".",".",".",".","2","8","."],
                        [".",".",".","4","1","9",".",".","5"],
                        [".",".",".",".","8",".",".","7","9"]])) # False
print(s.isValidSudoku([[".",".",".",".","5",".",".","1","."],
                        [".","4",".","3",".",".",".",".","."],
                        [".",".",".",".",".","3",".",".","1"],
                        ["8",".",".",".",".",".",".","2","."],
                        [".",".","2",".","7",".",".",".","."],
                        [".","1","5",".",".",".",".",".","."],
                        [".",".",".",".",".","2",".",".","."],
                        [".","2",".","9",".",".",".",".","."],
                        [".",".","4",".",".",".",".",".","."]])) # False