#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#
# https://leetcode.com/problems/unique-paths/description/
#
# algorithms
# Medium (52.84%)
# Likes:    3368
# Dislikes: 210
# Total Accepted:    492.8K
# Total Submissions: 914.5K
# Testcase Example:  '3\n2'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
#
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
#
# How many possible unique paths are there?
#
#
# Above is a 7 x 3 grid. How many possible unique paths are there?
#
#
# Example 1:
#
#
# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the
# bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
#
#
# Example 2:
#
#
# Input: m = 7, n = 3
# Output: 28
#
#
#
# Constraints:
#
#
# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.
#
#
#

# @lc code=start

# Idea: The following uses a recursive solution.
# Time Limited Exceeded for input: 23\n10
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
      memo = [[1] * n for _ in range(m)]

      for row in range(1,n):
        for col in range(1,m):
          memo[col][row] = memo[col-1][row] + memo[col][row-1]

      return memo[m-1][n-1]
# @lc code=end

class NaiiveSolution:
    def uniquePaths(self, m: int, n: int) -> int:

      # Seed with the bottom-right path
      # stored_paths = { (m-1, n-1): 0 }
      def get_path_value(col, row):

        # If we've already stored the paths, return it
        # if (m,n) in self.stored_paths:
          # return self.stored_paths[(m,n)]

        # If on right-most or bottom-most edge,
        # there can only be one path, store '1'.
        if (col,row) == (m-1, n-1):
          return 1
        if col == m-1 or row == n-1:
          # self.stored_paths[(col,row)] = 1
          return 1
        else:
          return get_path_value(col+1, row) + get_path_value(col, row+1)


      return get_path_value(0,0)

# print(Solution().uniquePaths(1,1))
print(Solution().uniquePaths(4,4))
print(Solution().uniquePaths(23,12))
