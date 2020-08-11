#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#
# https://leetcode.com/problems/power-of-four/description/
#
# algorithms
# Easy (41.50%)
# Likes:    665
# Dislikes: 236
# Total Accepted:    198.4K
# Total Submissions: 476.7K
# Testcase Example:  '16'
#
# Given an integer (signed 32 bits), write a function to check whether it is a
# power of 4.
#
# Example 1:
#
#
# Input: 16
# Output: true
#
#
#
# Example 2:
#
#
# Input: 5
# Output: false
#
#
# Follow up: Could you solve it without loops/recursion?
#

# @lc code=start
class Solution:
    def isPowerOfFour(self, num: int) -> bool:

      # Base case:
      if num == 1:
        return True # Because anything to the power of 0 is 1

      if num == 4:
        return True

      answer = 4
      while answer <= num:
        answer *= 4
        if answer == num:
          return True
      return False

# @lc code=end

