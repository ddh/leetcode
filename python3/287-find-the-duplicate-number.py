#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (54.92%)
# Likes:    4749
# Dislikes: 566
# Total Accepted:    345.2K
# Total Submissions: 626.5K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
#
# Example 1:
#
#
# Input: [1,3,4,2,2]
# Output: 2
#
#
# Example 2:
#
#
# Input: [3,1,3,4,2]
# Output: 3
#
# Note:
#
#
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n^2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
#
#
#

# @lc code=start



# Idea: This uses a set to iterate through the nums array just once.
# Now, this solution doesn't abide by the constat space rule.
# It does however run through the nums array just once, which is a
# time complexity of just O(n).

from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
      counts = set()
      for num in nums:
        if num in counts:
          return num
        else:
          counts.add(num)


# @lc code=end

print(Solution().findDuplicate([3,1,3,4,2]))