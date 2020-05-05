"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

from typing import List
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#       count = 1
#       sums = [nums[0]]

#       # Array of sums:
#       for i in range(1, len(nums)):
#         sums.append(sums[i - 1] + nums[i])

#       for i in range(len(nums)):
#         for j in range(len(nums)):
#           if sums[len(nums) - j - 1] - sums[i - 1] == k:
#             count += 1
#       return count


class Solution:
    def subarraySum(self, nums: List, k: int) -> int:

        count = 0
        total = 0
        sums_map = {}
        sums_map[0] = 1

        for num in nums:
            total += num
            if sums_map.get(total - k):
                count += sums_map.get(total - k)

            sums_map[total] = 1 + sums_map.get(total, 0)

        return count

print(Solution().subarraySum([1,1,1], 2))
print(Solution().subarraySum([1,1,2,2,3,4,5], 2))


