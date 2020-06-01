"""
 You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.

Example 2:

Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.

Note:

    All elements in nums1 and nums2 are unique.
    The length of both nums1 and nums2 would not exceed 1000.
"""

# Idea: Arrays have no duplicates

from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

      # Base case; second array empty
      if not nums2:
        return [-1] * len(nums1)

      next_greater_num_table = {}
      unprocessed_nums = [nums2[0]] # Prime with the first number from nums2

      for num in nums2[1:]:

        # If there are numbers in the stack, check if the current num is greater than it, then add it to the table
        while unprocessed_nums and unprocessed_nums[-1] < num:
          next_greater_num_table[unprocessed_nums.pop()] = num
        unprocessed_nums.append(num)

      # Notice that we still have a stack of unprocessed numbers.
      # We discard the stack and if we encounter a number from the
      # stack in nums1, we automatically assume -1, no greater num found.
      
      return [next_greater_num_table[num] if num in next_greater_num_table else -1 for num in nums1]

# Driver:
print(Solution().nextGreaterElement([4,1,2], [4,3,5,2,1]))
print(Solution().nextGreaterElement([4,1,2], []))