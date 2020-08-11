#
# @lc app=leetcode id=796 lang=python3
#
# [796] Rotate String
#
# https://leetcode.com/problems/rotate-string/description/
#
# algorithms
# Easy (49.73%)
# Likes:    738
# Dislikes: 52
# Total Accepted:    69.3K
# Total Submissions: 139.5K
# Testcase Example:  '"abcde"\n"cdeab"'
#
# We are given two strings, A and B.
#
# A shift on A consists of taking string A and moving the leftmost character to
# the rightmost position. For example, if A = 'abcde', then it will be 'bcdea'
# after one shift on A. Return True if and only if A can become B after some
# number of shifts on A.
#
#
# Example 1:
# Input: A = 'abcde', B = 'cdeab'
# Output: true
#
# Example 2:
# Input: A = 'abcde', B = 'abced'
# Output: false
#
#
# Note:
#
#
# A and B will have length at most 100.
#
#
#

# @lc code=start
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
      A_start, B_start = 0, 0

      for i in range(len(B)):
        if B[i] != A[0]:
          B_start += 1
      print(B_start)

# @lc code=end

