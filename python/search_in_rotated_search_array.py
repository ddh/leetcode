"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

"""
Idea:
The clue is the runtime O(log n), meaning binary search is involved.

But that's tricky if the array was rotate:
* When we choose the pivot, we can't guarantee all of the elements left of the pivot is < pivot. Vice versa right side.

We can do a modified search: pivot as normal, producing arrays a and b.

We know that:
1. if a[0] > a[-1], the rotation is in this array. Also, if target >= a[0] AND >= a[-1], we should pick this array to continue searching
2. if b[0] < b[-1], then this array is not affected by the rotation. Also, if target >= b[0] AND <= b[-1], it could be in here.
"""

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # start, end = 0, len(nums) - 1
        # while start <= end:
        #     mid = start + (end - start) // 2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[mid] >= nums[start]:
        #         if target >= nums[start] and target < nums[mid]:
        #             end = mid - 1
        #         else:
        #             start = mid + 1
        #     else:
        #         if target <= nums[end] and target > nums[mid]:
        #             start = mid + 1
        #         else:
        #             end = mid - 1
        return -1

class Solution2:
  def search(self, nums: List[int], target: int) -> int:
      start, end = 0, len(nums) - 1
      while start <= end:
        pivot = (start + end) // 2
        print(f'start: {start}, end: {end}, pivot: {pivot}')
        if nums[pivot] == target:
            return pivot
        elif nums[start] <= nums[pivot]:
          if target >= nums[start] and target <= nums[pivot]:
            end = pivot - 1
          else:
            start = pivot + 1
        else:
          if target > nums[pivot] and target <= nums[end]:
            start = pivot + 1
          else:
            end = pivot - 1
      return -1

# Driver:
print(Solution2().search([4,5,6,7,0,1,2], 0))
print(Solution2().search([4,5,6,7,0,1,2], 3))
print(Solution2().search([1,2,3], 2))

