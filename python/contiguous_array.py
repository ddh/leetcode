"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
"""

from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        counts = {}
        max = 0
        for index, num in enumerate(nums):
          for i in range(index + 1):
            if num == 1:
              counts[i] = counts.get(i, 0) + 1
            else:
              counts[i] = counts.get(i, 0) - 1
            distance = index + 1 - i
            if counts[i] == 0 and distance > max:
              max = distance
            print(f'counts on index {index}: {counts}, max: {max}, distance: {distance}')
        print()
        return max



# Driver
print(Solution().findMaxLength([0,0,1,0,0,0,1,1]))