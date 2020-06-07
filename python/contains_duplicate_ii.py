
"""
https://leetcode.com/problems/contains-duplicate-ii/

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

"""

# Idea: We basically want to find duplicates in the array. We just need to find two.
# However, there's a constraint; the distance between the pair needs to be no more than
# the value of k, as supplied by the problem.
# What we can do is keep a hashmap of the values we encounter. The element-value is the key
# whereas the indices are the values of the hashmap. When we encounter an element-value
# that already exists in the hashmap, we want to compare the indices and return TRUE
# if the absolute difference between the two indices is less than k. If not, replace
# the value in the hashmap with the new indices and continue onwards.

from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # Base case:
        if not nums:
          return False

        # Base case; can't have 0 distance between two indices. k has to be > 0
        if k <= 0:
          return False

        indices = {}
        for i, num in enumerate(nums):
          if num in indices:
            if abs(i - indices[num]) <= k:
              return True
          indices[num] = i
        
        return False



# Driver:
print(Solution().containsNearbyDuplicate([1,2,3,1], 3)) # true
print(Solution().containsNearbyDuplicate([1,0,1,1], 1)) # true
print(Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2)) # false