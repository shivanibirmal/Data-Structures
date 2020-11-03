# 212. Word Search II
# Hard

# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
#
#
# Example:
#
# Input:
# board = [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
#
# Output: ["eat","oath"]
#
#
# Note:
#
# All inputs are consist of lowercase letters a-z.
# The values of words are distinct.
from typing import List
import copy

class Solution:

    b = []

    row_directions = [1,-1,0,0]
    col_directions = [0,0,1,-1]

    total_rows = 0
    total_cols = 0

    words_found = []

    def dfs(self, row, col, w, idx):
        #idx is current index of word that we are trying to match
        if self.b[row][col] == w[idx]:

            if idx+1 == len(w):
                return True

            prefix = self.b[row][col]
            self.b[row][col] = 1 #mark as visited

            for i in range(0,4):
                next_row = row + self.row_directions[i]
                next_col = col + self.col_directions[i]

                if next_row >= 0 and next_row < self.total_rows and next_col >= 0 and next_col < self.total_cols:
                    dfs_result = self.dfs(next_row, next_col, w, idx+1)
                    if dfs_result:
                        return True

            #word was not found and hence, control is outside for loop.
            # at this point, we need to backtrack i.e.remove the marked 1's from the board

            self.b[row][col] = prefix
        # print("board in dfs:", board)
        return False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        initial_board = copy.deepcopy(board[:])
        print("outside initial_board:", initial_board)
        self.b = board
        self.total_rows = len(board)
        self.total_cols = len(board[0])


        for word in words:
            print("word to be found:", word)
            self.b = copy.deepcopy(initial_board)
            # print("current board for finding new word:", self.b)
            for row in range(0, self.total_rows):
                for col in range(0, self.total_cols):
                    dfs_result = self.dfs(row, col, word, 0)

                    if dfs_result:
                        # print("word found:", word)
                        # print("current board after finding word:", self.b)
                        # print("current initial_board after finding word:", initial_board)
                        self.words_found.append(word)
                        break
                        # return True
                break
        return self.words_found

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
word = ["eat","oath"]

solution = Solution()
print("words found:", solution.findWords(board, word))
