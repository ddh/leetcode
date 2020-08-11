#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three/description/
#
# algorithms
# Easy (42.03%)
# Likes:    543
# Dislikes: 1493
# Total Accepted:    270K
# Total Submissions: 641.8K
# Testcase Example:  '27'
#
# Given an integer, write a function to determine if it is a power of three.
#
# Example 1:
#
#
# Input: 27
# Output: true
#
#
# Example 2:
#
#
# Input: 0
# Output: false
#
# Example 3:
#
#
# Input: 9
# Output: true
#
# Example 4:
#
#
# Input: 45
# Output: false
#
# Follow up:
# Could you do it without using any loop / recursion?
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:

      # Base case:
      if n == 1:
        return True # Because anything to the power of 0 is 1

      if n == 3:
        return True

      answer = 3
      while answer <= n:
        answer *= 3
        if answer == n:
          return True
      return False

# @lc code=end

