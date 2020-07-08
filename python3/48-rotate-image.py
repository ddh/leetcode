#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
# https://leetcode.com/problems/rotate-image/description/
#
# algorithms
# Medium (55.79%)
# Likes:    3000
# Dislikes: 227
# Total Accepted:    405.4K
# Total Submissions: 725.5K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# You are given an n x n 2D matrix representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# Note:
#
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.
#
# Example 1:
#
#
# Given input matrix =
# [
# ⁠ [1,2,3],
# ⁠ [4,5,6],
# ⁠ [7,8,9]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
# ⁠ [7,4,1],
# ⁠ [8,5,2],
# ⁠ [9,6,3]
# ]
#
#
# Example 2:
#
#
# Given input matrix =
# [
# ⁠ [ 5, 1, 9,11],
# ⁠ [ 2, 4, 8,10],
# ⁠ [13, 3, 6, 7],
# ⁠ [15,14,12,16]
# ],
#
# rotate the input matrix in-place such that it becomes:
# [
# ⁠ [15,13, 2, 5],
# ⁠ [14, 3, 4, 1],
# ⁠ [12, 6, 8, 9],
# ⁠ [16, 7,10,11]
# ]
#
#
#

# @lc code=start

# Idea: We will keep a temporary list of letters, and rotate clockwise.
# We'll do this for the outer loop, then the loop inside.
# If the size of n is odd, we know that the very center of the grid
# is by itself and would not need rotating. If n is even, then we will
# rotate n times in the outer loop.

from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix[0])
        temp_start = 0
        temp_end = n - 1

        # We iterate the outer loop half the width of grid (eg n//2 for a nxn grid):
        while temp_start < (n // 2):


          # Prime the temp array
          # print(f'temp_start: {temp_start}')
          temp = matrix[temp_start][temp_start:temp_end]
          # print(f'temp: {temp}')

          # Right col temp (reads top-down)
          # print('right col:')
          for i, row in enumerate(matrix[temp_start:temp_end]):
            temp[i], row[temp_end] = row[temp_end], temp[i]
          # print(f'temp: {temp}')

          # Bottom row temp (reads right-left)
          # print('bottom row:')
          for i in range(temp_end-temp_start):
            temp[i], matrix[temp_end][temp_end-i] = matrix[temp_end][temp_end-i], temp[i]
          # print(f'temp: {temp}')

          # Left col temp (reads bottom-up)
          # print('left col:')
          for i in range(temp_end-temp_start):
            temp[i], matrix[temp_end-i][temp_start] = matrix[temp_end-i][temp_start], temp[i]
          # print(f'temp: {temp}')

          # Swap the top row:
          # print('top row:')
          for i in range(temp_end-temp_start):
            temp[i], matrix[temp_start][temp_start+i] = matrix[temp_start+i][i], temp[i]
          # print(f'temp: {temp}')

          # Shorten the temp array length
          temp_start += 1
          temp_end -= 1

          # print(f'temp_start: {temp_start}')
          # print()

        # # Debugging
        # for row in matrix:
        #   print(row)




# @lc code=end

# print(Solution().rotate([ [1,2,3], [4,5,6], [7,8,9] ]))
print(Solution().rotate([ ['a','b','c','d','e'], ['f','g','h','i','j'], ['k','l','m','n','o'], ['p','q','r','s','t'], ['u','v','w','x','y'] ]))