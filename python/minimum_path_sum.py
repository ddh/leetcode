"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

# Idea:


from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

      # To save space, we can update each cell in-place
      # Update the first row and first "col" with the sum from previous cell

      # We update the current cell with its value + the min between
      # the value immediately above and immediately left
      print(grid[0])
      print(grid[1])
      print(grid[2])
      print()
      for y, row in enumerate(grid):
        # Setting first column:
        if y >= 1:
          grid[y][0] += grid[y - 1][0]
        for x, col in enumerate(row):
          # Setting first row
          print(f'x: {x}, y: {y}')
          if y == 0 and x >= 1:
            grid[x][y] += grid[x][y - 1]
          elif x >= 1 and y >= 1:
            grid[x][y] += min(grid[x - 1][y], grid[x][y - 1])
          print(grid[0])
          print(grid[1])
          print(grid[2])
          print()

      # 3. All done! With the grid filled, return the bottom-right value:
      return grid[-1][-1]

# Driver
print(Solution().minPathSum([[1,3,1],[1,5,1],[4,2,1]]))