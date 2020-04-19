"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

from typing import List
class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    final_product = [1]

    for i, num in enumerate(nums[:-1]):
      final_product.append(final_product[i] * num)

    running_right_product = 1
    for i, num in enumerate(reversed(nums[1:])):
      running_right_product *= num
      final_product[len(nums) - i - 2] *= running_right_product
    return final_product

# Driver
print(Solution().productExceptSelf([1,2,3,4])) # [24,12,8,6]