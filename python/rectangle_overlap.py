"""
https://leetcode.com/problems/rectangle-overlap/

A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the coordinates of its bottom-left corner, and (x2, y2) are the coordinates of its top-right corner.

Two rectangles overlap if the area of their intersection is positive.  To be clear, two rectangles that only touch at the corner or edges do not overlap.

Given two (axis-aligned) rectangles, return whether they overlap.

Example 1:

Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
Output: true

Example 2:

Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
Output: false

Notes:

    Both rectangles rec1 and rec2 are lists of 4 integers.
    All coordinates in rectangles will be between -10^9 and 10^9.

"""

# Idea: Draw it out on a whiteboard. Ensure that the x and y of first rectangle is within the bounds of the other rectangle's edges
# Note that coordinates are always bottom-left corner then followed by top-right corner, always. Helps you make assumptions

from typing import List
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:


      # x1, y1, x2, y2 = rec1
      # x_1, y_1, x_2, y_2 = rec2

      return not ( (rec1[0] >= rec2[2]) or (rec1[2] <= rec2[0]) or (rec1[1] >= rec2[3]) or (rec1[3] <= rec2[1]) )

# Driver:
print(Solution().isRectangleOverlap([0,0,2,2], [1,1,3,3])) # True
print(Solution().isRectangleOverlap([0,0,1,1], [1,0,2,1])) # False
print(Solution().isRectangleOverlap([7,8,13,15], [10,8,12,20])) # True
print(Solution().isRectangleOverlap([2,17,6,20], [3,8,6,20])) # True




