#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (33.65%)
# Likes:    1379
# Dislikes: 1942
# Total Accepted:    571.1K
# Total Submissions: 1.7M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
#
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
#
# Example 1:
#
#
# Input: 4
# Output: 2
#
#
# Example 2:
#
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
# the decimal part is truncated, 2 is returned.
#
#
#

# @lc code=start

# Idea: We know that we're looking for the integer square root. So it's the closet we can get to the
# actual square root, without going over. We know that the number is larger than 0, but smaller than half of
# x. So say `a` is the answer, then 0 < a < (x/2). We know that when x=0 then a=0, x=1 then a=1, x=2 then a=1.
# Anything after 2, we can use 0 < a < (x/2). We'll do a binary search and check if the pivot, when squared,
# then truncated, equals the answer. If no, and the square is larger than the target, then we need to look left.
# Conversely, if the square is smaller than the target, we'll need to resume looking right

class Solution:
    def mySqrt(self, x: int) -> int:

      # Base cases:
      if x == 0:
        return 0
      if x in [1,2,3]:
        return 1

      l = 0
      r = x

      while l < r:
        mid = l + (r-l) // 2
        if mid ** 2 <= x < (mid + 1) ** 2:
          return mid
        elif mid ** 2 > x:
          r = mid
        else:
          l = mid + 1
# @lc code=end

print(Solution().mySqrt(4))
print(Solution().mySqrt(5))
print(Solution().mySqrt(6))