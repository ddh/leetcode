#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#
# https://leetcode.com/problems/arranging-coins/description/
#
# algorithms
# Easy (39.93%)
# Likes:    657
# Dislikes: 710
# Total Accepted:    164.7K
# Total Submissions: 393.5K
# Testcase Example:  '5'
#
# You have a total of n coins that you want to form in a staircase shape, where
# every k-th row must have exactly k coins.
# ⁠
# Given n, find the total number of full staircase rows that can be formed.
#
# n is a non-negative integer and fits within the range of a 32-bit signed
# integer.
#
# Example 1:
#
# n = 5
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
#
# Because the 3rd row is incomplete, we return 2.
#
#
#
# Example 2:
#
# n = 8
#
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
#
# Because the 4th row is incomplete, we return 3.
#
#
#

# Idea: Iterative approach; we keep adding +1 to the number of steps needed. We subtract this from n
# in a loop. As long as we still have n coins, we can continue to subtract. For each time we subtract,
# we keep count of the number of successful subtractions we do. This count will be the number of steps.

# @lc code=start
class Solution:
    def arrangeCoins(self, n: int) -> int:
      coins_needed = 1
      steps_achieved = 0


      while n >= 0:
        n -= coins_needed
        if n >= 0:
          steps_achieved += 1
        coins_needed += 1

      return steps_achieved

# @lc code=end

