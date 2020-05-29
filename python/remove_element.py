"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,1,2,2,3,0,4,2], val = 2,

Your function should return length = 5, with the first five elements of nums containing 0, 1, 3, 0, and 4.

Note that the order of those five elements can be arbitrary.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeElement(nums, val);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

# Idea: Keep a pointer at both ends. Whenever the target value is detected in the front of array, swap it with the pointer at the end.
# Though, we must be sure that the pointer at the end is not pointing at the target value, so move the end pointer to the left until
# it isn't pointing to the target value

from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

      # Base case:
      if len(nums) == 1:
        if nums[0] != val:
          print(nums)
          return 1

      tail_pointer = len(nums) - 1
      head_pointer = 0
      while head_pointer <= tail_pointer:
        while tail_pointer >= 0 and nums[tail_pointer] == val:
          tail_pointer -= 1
        if tail_pointer < head_pointer:
          break
        if nums[head_pointer] == val:
          nums[head_pointer], nums[tail_pointer] = nums[tail_pointer], nums[head_pointer]
        head_pointer += 1

      # Another base case. If head_pointer never incremented, that means the tail_pointer kept
      # encountering the target all the way through the array. There's no elements to swap, so
      # we must empty the original array in place.
      if head_pointer == 0:
        del nums[:]

      return head_pointer


# Driver:
print(Solution().removeElement([3,2,2,3], 3)) # 2
print(Solution().removeElement([0,1,2,2,3,0,4,2], 2)) # 5
print(Solution().removeElement([2], 3)) # 1
print(Solution().removeElement([3,3], 3)) # 3