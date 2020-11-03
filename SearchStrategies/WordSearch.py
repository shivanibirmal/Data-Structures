# 79. Word Search
# Medium
#
# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# Example:
#
# board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
#
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
#
#
# Constraints:
#
# board and word consists only of lowercase and uppercase English letters.
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
from typing import List


class Solution:

    b = []
    w = []

    row_directions = [1,-1,0,0]
    col_directions = [0,0,1,-1]

    total_rows = 0
    total_cols = 0

    def dfs(self, row, col, idx):
        #idx is current index of word that we are trying to match
        if self.b[row][col] == self.w[idx]:

            if idx+1 == len(self.w):
                return True

            prefix = self.b[row][col]
            self.b[row][col] = 1 #mark as visited

            for i in range(0,4):
                next_row = row + self.row_directions[i]
                next_col = col + self.col_directions[i]

                if next_row >= 0 and next_row < self.total_rows and next_col >= 0 and next_col < self.total_cols:
                    dfs_result = self.dfs(next_row, next_col, idx+1)
                    if dfs_result:
                        return True

            #word was not found and hence, control is outside for loop.
            # at this point, we need to backtrack i.e.remove the marked 1's from the board

            self.b[row][col] = prefix

        return False

    def exist(self, board: List[List[str]], word: str) -> bool:

        self.b = board
        self.w = word

        self.total_rows = len(board)
        self.total_cols = len(board[0])

        for row in range(0, self.total_rows):
            for col in range(0, self.total_cols):
                dfs_result = self.dfs(row, col, 0)

                if dfs_result:
                    return True
        return False

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "SEE"

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
word = "eat"

solution = Solution()
print("word found:",solution.exist(board, word))
