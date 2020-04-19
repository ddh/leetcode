"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""

from typing import List

# Time Limit Exceeded
class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        lands = []
        islands = 0

        for i, row in enumerate(grid):
          for j, column in enumerate(row):
            if column == "1": lands.append((i, j))

        while lands:
          islands += self.explore(lands[0], lands)

        return islands

    def explore(self, target, lands):
      lands.remove(target)
      if (target[0], target[1] + 1) in lands:
        self.explore((target[0], target[1] + 1), lands)
      if (target[0], target[1] - 1) in lands:
        self.explore((target[0], target[1] - 1), lands)
      if (target[0] + 1, target[1]) in lands:
        self.explore((target[0] + 1, target[1]), lands)
      if (target[0] - 1, target[1]) in lands:
        self.explore((target[0] - 1, target[1]), lands)
      return 1

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    island_count = 0

    for x, row in enumerate(grid):
      for y, col in enumerate(grid[x]):
        if grid[x][y] == "1":
          self.explore(grid, x, y)
          island_count += 1
    return island_count

  def explore(self, grid, x, y):

    # Mark as visited
    grid[x][y] = "0"

    # Look up
    if y - 1 >= 0 and grid[x][y - 1] == "1":
      self.explore(grid, x, y - 1)
    # Look down
    if y + 1 < len(grid[0]) and grid[x][y + 1] == "1":
      self.explore(grid, x, y + 1)
    # Look right
    if x + 1 < len(grid) and grid[x + 1][y] == "1":
      self.explore(grid, x + 1, y)
    # Look left
    if x - 1 >= 0 and grid[x - 1][y] == "1":
      self.explore(grid, x - 1, y)

# Driver:
print(Solution().numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
print(Solution().numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
print(Solution().numIslands([["1","1","1"],["0","1","0"],["1","1","1"]]))

# print(Solution2().numIslands([["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
# print(Solution2().numIslands([["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
