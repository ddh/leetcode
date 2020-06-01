"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:

    You may assume that the array does not change.
    There are many calls to sumRange function.
"""

from typing import List

class NumArray:

    def __init__(self, nums: List[int]):

      self.cumulative_sums = {}

      # Base case when nums is empty:
      if nums:
        # Make a hashtable, keeping a cache of the cumulative sums from 0 to i
        self.cumulative_sums[(0,0)] = nums[0]
        for i, num in enumerate(nums[1:]):
          previous_sum = self.cumulative_sums[(0,i)]
          self.cumulative_sums[(0,i+1)] =  previous_sum + nums[i+1]

    def sumRange(self, i: int, j: int) -> int:
      if not self.cumulative_sums:
        return None

      sum_from_0_to_j = self.cumulative_sums[(0,j)]

      if i == 0:
        return sum_from_0_to_j
      else:
        sum_from_0_to_i = self.cumulative_sums[(0,i - 1)]
        return sum_from_0_to_j - sum_from_0_to_i



# Driver:

# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0,2))
print(obj.sumRange(2,5))
print(obj.sumRange(0,5))

