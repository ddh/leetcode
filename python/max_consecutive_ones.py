"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
      max_ones_count = 0
      current_ones_count = 0
      for num in nums:
        if num == 1:
          current_ones_count += 1
          if current_ones_count > max_ones_count:
            max_ones_count = current_ones_count
        else:
          current_ones_count = 0
      return max_ones_count

# Driver
print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))
