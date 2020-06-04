"""
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.



Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16

Explanation: The perimeter is the 16 yellow stripes in the image below:


"""

# Idea: We'll iterate through each cell by row then column. Whenever we encounter a piece of land,
# we know that it starts out with a perimeter of 4. For every neighbor that land has, we need to
# subtract away 1 perimeter. So let's do this for each cell and add on whatever remaining perimeter
# each cell has. In the end, we'll have come up with our answer.
# Time: We iterate through each cell so O(m*n) to start. For each cell, at worst all cells are land,
# we'll check in each of the directions. So in the end it'd be O(4*m*n) or just O(m*n).

from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
      total_perimeter = 0

      for i, row in enumerate(grid):
        for j, col in enumerate(row):
          # print(f'i: {i}, j: {j}, land?: {grid[i][j]}') # Debugging
          if grid[i][j] == 1:
            current_perimeter = 4
            # Look up
            if 0 <= i-1 <= len(grid) - 1 and grid[i-1][j] == 1:
              current_perimeter -= 1
            # Look right
            if 0 <= j+1 <= len(grid[0]) - 1 and grid[i][j+1] == 1:
              current_perimeter -= 1
            # Look down
            if 0 <= i+1 <= len(grid) - 1 and grid[i+1][j] == 1:
              current_perimeter -= 1
            # Look left
            if 0 <= j-1 <= len(grid[0]) - 1 and grid[i][j-1] == 1:
              current_perimeter -= 1
            total_perimeter += current_perimeter

      return total_perimeter

# Driver:
print(Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])) # 16