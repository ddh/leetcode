"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75


Note:

1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
"""

# Idea: We're going to use a sliding window. Good that we know k, the length of the subarray.
# We will slide the window along and compute the SUM as we go. No need to compute the average
# until the very end since what we're looking for is the largest sum that will thus give
# us the largest average. To get the new sum, we subtract the element we slide away from on the left,
# then add the value from the element we slid into on the right

from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

      # Keep pointers at opposites ends of sliding window
      start = 0
      end = k - 1

      current_sum = sum(nums[:k])
      max_sum = current_sum

      while end < len(nums) - 1:
        current_sum -= nums[start] # Subtract the left element
        current_sum += nums[end + 1] # Tack on the right element
        max_sum = max(max_sum, current_sum) # Keep the largest sum we've encountered so far
        # Moving the window up
        start += 1
        end += 1
      return max_sum / k

# Driver
print(Solution().findMaxAverage([1,12,-5,-6,50,3], 4)) # 12.75