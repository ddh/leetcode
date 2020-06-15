"""
https://leetcode.com/problems/rotate-array/

Given an array, rotate the array to the right by k steps, where k is non-negative.

Follow up:

    Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
    Could you do it in-place with O(1) extra space?



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]



Constraints:

    1 <= nums.length <= 2 * 10^4
    It's guaranteed that nums[i] fits in a 32 bit-signed integer.
    k >= 0


"""

# IDea:

from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        steps = k % len(nums)

        # Base case: If k is the length of the array OR k is a multiple of the length of the array, we don't need to rotate
        if steps == 0:
          return nums

        temp = None
        index = 0
        count = 0
        length = len(nums)

        while count < length:

          temp, nums[index] = nums[index], temp
          index = (index + steps) % length
          if nums[index] is None:
            temp, nums[index] = nums[index], temp
            index = (index + 1) % length
          count += 1

          print(f'{nums}, temp: {temp}, pointer: {index} ({nums[index]})')





# Driver:
print(Solution().rotate([1,2,3,4,5,6,7], 3)) # [5,6,7,1,2,3,4]
print(Solution().rotate(['A','B','C','D'], 2)) # [3,99,-1,-100]
print(Solution().rotate([1,2,3,4,5], 3)) # [5,6,7,1,2,3,4]


