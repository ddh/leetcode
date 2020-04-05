"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      int_dict = {}
      for num in nums:
        int_dict[num] = int_dict.get(num, 0) + 1
      for num, count in int_dict.items():
        if count == 1:
          return num

# Driver
print(Solution().singleNumber([2,2,1]))