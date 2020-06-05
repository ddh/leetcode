"""
Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.


Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].
"""

# Idea: perform a binary search

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
      # Base case, one element:
      if len(nums) == 1:
        return 0 if nums[0] == target else -1

      start, end = 0, len(nums) - 1

      while start <= end:
        midpoint = (end - start) // 2 + start
        if nums[midpoint] == target:
          return midpoint
        elif nums[midpoint] < target:
          start = midpoint + 1
        else:
          end = midpoint - 1
      return -1

# Driver:
print(Solution().search([-1,0,3,5,9,12], 9)) # 4
print(Solution().search([-1,0,3,5,9,12], 2)) # -1
print(Solution().search([9], 9)) # 0
print(Solution().search([9], 7)) # -1
print(Solution().search([2,5], 5)) # 1