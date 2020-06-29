#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Easy (41.87%)
# Likes:    4675
# Dislikes: 143
# Total Accepted:    512.6K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
#
#
# Example 2:
#
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
#
#
# Constraints:
#
#
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 400
#
#
#

# @lc code=start

# Idea: This is another one of those DP problems, similar to fibonacci.
# Try keeping a memo of previous maximum. Iterate through the elements
# and determine the maximum encountered so far.
# The tricky part is the rule where a robber cannot rob two adjacent houses,
# or said in another way, no two houses in a row cannot be chosen.
# 
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:

      # Base case: len == 0
      if not nums:
        return 0

      # Base case: len == 1
      if len(nums) == 1:
        return nums[0]

      # Base case: len == 2
      if len(nums) == 2:
        return max(nums[0], nums[1])

      memo = [None] * len(nums)
      memo[0] = nums[0]
      memo[1] = max(nums[0], nums[1])
      counter = 2

      while counter < len(nums):
        memo[counter] = max(memo[counter - 1], memo[counter - 2] + nums[counter])
        counter += 1

      return memo[-1]



# @lc code=end

print(Solution().rob([2,7,9,3,1]))
print(Solution().rob([1,2,3,1]))
print(Solution().rob([1]))
print(Solution().rob([1,5]))
print(Solution().rob([5,10,4]))
print(Solution().rob([5,10,4,1]))
print(Solution().rob([2,1,1,2]))