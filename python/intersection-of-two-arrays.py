"""
https://leetcode.com/problems/intersection-of-two-arrays/

349. Intersection of Two Arrays
Easy

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:

    Each element in the result must be unique.
    The result can be in any order.
"""

# Idea: lucky that the elements in the result are unique. This means
# we can implement a hashmap and count both arrays. Then we take the smaller
# hashmap of the two (size in keys) and iterate through each, checking against the
# other hashmap and then inserting into an answer array.

from typing import List
from collections import Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

      # Count occurrences
      nums1_counts = Counter(nums1)
      nums2_counts = Counter(nums2)

      # Swap so nums1_counts will always be the smaller to make it easier to iterate through
      if len(nums1_counts) > len(nums2_counts):
        nums1_counts, nums2_counts = nums2_counts, nums1_counts

      return [num for num in nums1_counts if num in nums2_counts]




# Driver:
print(Solution().intersection([1,2,2,1], [2,2])) # [2]
print(Solution().intersection([4,9,5], [9,4,9,8,4])) # [9,4]


