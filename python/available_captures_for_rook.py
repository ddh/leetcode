"""
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.
"""

from typing import List
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:

      # Search for the rook first
      rook_position = (-1, -1)
      for row, y in enumerate(board):
        for col, x in enumerate(y):
          if board[row][col] == 'R':
            rook_position = (row, col)

      # Instructions to move up, right, down, left on the board
      move_up, move_right, move_down, move_left = (-1, 0), (0, 1), (1, 0), (0, -1)

      # provide the rook's current position and row&col direction to move
      def dfs_with_direction(current_row, current_col, move_row, move_col):
        new_position = (current_row + move_row, current_col + move_col)

        # Check if new position is within the board
        if 0 <= new_position[0] <= len(board) - 1 and 0 <= new_position[1] <= len(board[0]) - 1:

          # When encountering a Biship, there are no kills
          if board[new_position[0]][new_position[1]] == 'B':
            return 0
          # When encountering empty cell, recursively call dfs in the same direction
          if board[new_position[0]][new_position[1]] == '.':
            return dfs_with_direction(*new_position, *(move_row, move_col))
          # When encountering a pawn, return the kill count of 1
          if board[new_position[0]][new_position[1]] == 'p':
            return 1
        else:
          return 0

      # Check if we've killed a pawn in each cardinal direction
      kills = [
        dfs_with_direction(*rook_position, *move_up),
        dfs_with_direction(*rook_position, *move_right),
        dfs_with_direction(*rook_position, *move_down),
        dfs_with_direction(*rook_position, *move_left),
        ]

      return sum(kills)

# Driver:
print(Solution().numRookCaptures([[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]])) # 3
