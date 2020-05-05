"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
"""

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if matrix is None or len(matrix) < 1:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0]*(cols+1) for _ in range(rows+1)]
        max_side = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    dp[r+1][c+1] = min(dp[r][c], dp[r+1][c], dp[r][c+1]) + 1 # Be careful of the indexing since dp grid has additional row and column
                    max_side = max(max_side, dp[r+1][c+1])

        return max_side * max_side

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        # Base condition:
        if matrix is None or len(matrix) == 0:
          return 0

        row_count = len(matrix)
        col_count = len(matrix[0])

        max_length = 0
        memoized_square_sizes = [[0] * col_count + 1 for i, row in range(row_count + 1)]

        for row in range(row_count):
            for col in range(col_count):
                if matrix[row][col] == '1':
                    memoized_square_sizes[row + 1][col + 1] = min(memoized_square_sizes[row][col], memoized_square_sizes[row + 1][col], memoized_square_sizes[row][col + 1]) + 1
                    max_length = max(max_length, memoized_square_sizes[row + 1][col + 1])

        return max_length * max_length

        # Largest square

