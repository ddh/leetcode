#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#
# https://leetcode.com/problems/set-mismatch/description/
#
# algorithms
# Easy (42.03%)
# Likes:    658
# Dislikes: 300
# Total Accepted:    73.5K
# Total Submissions: 174.6K
# Testcase Example:  '[1,2,2,4]'
#
#
# The set S originally contains numbers from 1 to n. But unfortunately, due to
# the data error, one of the numbers in the set got duplicated to another
# number in the set, which results in repetition of one number and loss of
# another number.
#
#
#
# Given an array nums representing the data status of this set after the error.
# Your task is to firstly find the number occurs twice and then find the number
# that is missing. Return them in the form of an array.
#
#
#
# Example 1:
#
# Input: nums = [1,2,2,4]
# Output: [2,3]
#
#
#
# Note:
#
# The given array size will in the range [2, 10000].
# The given array's numbers won't have any order.
#
#
#

# @lc code=start

# Idea: We should sort first before doing anything.
# Then we can iterate through each number
# Sorting is time complexity O(nlogn)
# while iterating through n times so O(n + nlogn) => O(nlogn) time complexity
# And O(logn) space for recursion that takes place in the sorting algo
from typing import List
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
      nums.sort()

      duplicate_num = None
      missing_num = None

      # # Base case:
      if len(nums) == 2 and nums[0] == 1:
        return [1,2]

      if nums[0] != 1:
        missing_num = 1

      for i, _ in enumerate(nums[:-1]):
        if nums[i] == nums[i+1]:
          duplicate_num = nums[i]
        if nums[i+1] - nums[i] > 1:
          missing_num = nums[i] + 1

      # Missing the last number:
      if not missing_num:
        missing_num = len(nums)

      return [duplicate_num, missing_num]
# @lc code=end

Solution().findErrorNums([2,1,5,4,6,2])