#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
#
# https://leetcode.com/problems/base-7/description/
#
# algorithms
# Easy (46.04%)
# Likes:    224
# Dislikes: 147
# Total Accepted:    54.4K
# Total Submissions: 118.2K
# Testcase Example:  '100'
#
# Given an integer, return its base 7 string representation.
#
# Example 1:
#
# Input: 100
# Output: "202"
#
#
#
# Example 2:
#
# Input: -7
# Output: "-10"
#
#
#
# Note:
# The input will be in range of [-1e7, 1e7].
#
#

# @lc code=start

# Idea: The algorithm to convert from base 10 to another, is to divide the number by the target-base. Whatever is the remainder,
# push it to a stack. Then take the dividend and repeat the process. You stop when the dividend is 0, then push the remainder
# into the stack one last time. Take the stack and reverse it, that is the answer.
class Solution:
    def convertToBase7(self, num: int) -> str:

      # Base case: 0
      if num == 0:
        return "0"

      base = 7
      negative = num < 0
      dividend = num if not negative else -num
      remainder = 0
      stack = []

      while dividend > 0:
        remainder = dividend % base
        stack.append(remainder)
        dividend = dividend // base

      # Need to convert each digit into a string
      stack = [str(digit) for digit in stack]

      # Then reverse and join them
      stack = "".join(stack[::-1])

      # And change sign if was negative to begin with
      return "-" + stack if negative else stack

# @lc code=end

# Driver:
print(Solution().convertToBase7(100)) # 202
print(Solution().convertToBase7(-7)) # -10

