"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      current_sum = nums[0]
      largest_sum = nums[0]
      for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        largest_sum = max(current_sum, largest_sum)
      return largest_sum


print([1,2,3,4,5,6,7,8,9][-4:])
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray([2,1,-3,-4,-1,2,1,5,4]))
print(Solution().maxSubArray([99,-10,-3,-70,-1,2,1,-5,-100]))
print(Solution().maxSubArray([-1]))
print(Solution().maxSubArray([0]))
print(Solution().maxSubArray([-2,1]))