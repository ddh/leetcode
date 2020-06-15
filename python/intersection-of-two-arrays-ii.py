"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/

350. Intersection of Two Arrays II
Easy

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:

    Each element in the result should appear as many times as it shows in both arrays.
    The result can be in any order.

Follow up:

    What if the given array is already sorted? How would you optimize your algorithm?
    What if nums1's size is small compared to nums2's size? Which algorithm is better?
    What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""

# Idea: Similar to the first `intersection of two arrays` problem.

from typing import List
from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Ensures nums1 is shorter so we can iterate better
        if len(nums1) > len(nums2):
          nums1, nums2 = nums2, nums1

        # Count the occurrences
        nums2_counts = Counter(nums2)

        answers = []
        for num in nums1:
          if num in nums2_counts and nums2_counts[num] > 0:
            nums2_counts[num] -= 1
            answers.append(num)

        return answers

# Driver:
print(Solution().intersect([1,2,2,1], [2,2])) # [2,2]
print(Solution().intersect([4,9,5], [9,4,9,8,4])) # [4,9]