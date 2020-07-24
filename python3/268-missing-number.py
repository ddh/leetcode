#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (51.33%)
# Likes:    1782
# Dislikes: 2101
# Total Accepted:    461.1K
# Total Submissions: 894.5K
# Testcase Example:  '[3,0,1]'
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
#
# Example 1:
#
#
# Input: [3,0,1]
# Output: 2
#
#
# Example 2:
#
#
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
#
#
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
#

# @lc code=start

# Idea: Take the sum formula for n. Then sum up the given array. Subtract the diff to find answers.

from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:

      # Formula for sum of n:  n(n+1) // 2
      n = len(nums)
      target_sum = n * (n+1) // 2
      nums_sum = sum(nums)
      return target_sum - nums_sum


# @lc code=end

