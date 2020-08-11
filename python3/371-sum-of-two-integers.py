#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Easy (50.68%)
# Likes:    1287
# Dislikes: 2279
# Total Accepted:    192.2K
# Total Submissions: 379.2K
# Testcase Example:  '1\n2'
#
# Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.
#
#
# Example 1:
#
#
# Input: a = 1, b = 2
# Output: 3
#
#
#
# Example 2:
#
#
# Input: a = -2, b = 3
# Output: 1
#
#
#
#
#

# @lc code=start

# Idea: I know I need to do bit-wise manipulation. But when am I going to be asked this as a full-stack? :(

class Solution:
    def getSum(self, a: int, b: int) -> int:
      # Base cases:
      if a == 0:
        return b
      if b == 0:
        return a
      if a == b:
        return 2 * a # Kinda cheating, is it?

      while b != 0:
        left_bit = (a & b) << 1
        a = a ^ b
        b = left_bit
      return a


# @lc code=end

