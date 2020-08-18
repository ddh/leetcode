#
# @lc app=leetcode id=1365 lang=python3
#
# [1365] How Many Numbers Are Smaller Than the Current Number
#
# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
#
# algorithms
# Easy (85.18%)
# Likes:    814
# Dislikes: 24
# Total Accepted:    103.4K
# Total Submissions: 120.7K
# Testcase Example:  '[8,1,2,2,3]'
#
# Given the array nums, for each nums[i] find out how many numbers in the array
# are smaller than it. That is, for each nums[i] you have to count the number
# of valid j's such that j != i and nums[j] < nums[i].
#
# Return the answer in an array.
#
#
# Example 1:
#
#
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]
# Explanation:
# For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3).
# For nums[1]=1 does not exist any smaller number than it.
# For nums[2]=2 there exist one smaller number than it (1).
# For nums[3]=2 there exist one smaller number than it (1).
# For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
#
#
# Example 2:
#
#
# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]
#
#
# Example 3:
#
#
# Input: nums = [7,7,7,7]
# Output: [0,0,0,0]
#
#
#
# Constraints:
#
#
# 2 <= nums.length <= 500
# 0 <= nums[i] <= 100
#
#

# @lc code=start
from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

      if not nums:
        return None

      if len(nums) == 1:
        return 0

      sorted_nums = sorted(nums) # Builds new sorted list from Iterable
      # sort(nums) # This is in-place sort
      counts = {}

      pointer = 0
      while pointer < len(sorted_nums):
        if sorted_nums[pointer] not in counts:
          counts[sorted_nums[pointer]] = pointer
        pointer += 1
      print(counts)

      return [counts[num] for num in nums]


# @lc code=end

Solution().smallerNumbersThanCurrent([8,1,2,2,3])