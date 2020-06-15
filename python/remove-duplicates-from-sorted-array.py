"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.

Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
"""

# Idea: The array is already sorted. We need to modify the array in place.
# Have a pointer indicate where we're currently at. The fast pointer will
# move along the array and whenever the fast pointer points to an element
# that is not the same as the value of the slow pointer's, we will increment
# the slow pointer by one and set the value to whatever the fast pointer was.
# We will do this until the fast pointer hits the end of the array.

# And of course, check for base cases like if the list is empty and what not.
# Base case shoudl check in the case all elements are the same value. The length
# in this case should be '1' and there are no modifications to the original array.


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

      slow_pointer = 0
      fast_pointer = 0

      while fast_pointer <= len(nums) - 1:
        if nums[slow_pointer] != nums[fast_pointer]:
          slow_pointer += 1
          nums[slow_pointer] = nums[fast_pointer]
        fast_pointer += 1
      return slow_pointer + 1

# Driver:
print(Solution().removeDuplicates([1,1,2])) # 2
print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5