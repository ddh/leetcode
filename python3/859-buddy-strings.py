#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#
# https://leetcode.com/problems/buddy-strings/description/
#
# algorithms
# Easy (27.55%)
# Likes:    575
# Dislikes: 397
# Total Accepted:    48.3K
# Total Submissions: 176.3K
# Testcase Example:  '"ab"\n"ba"'
#
# Given two strings A and B of lowercase letters, return true if and only if we
# can swap two letters in A so that the result equals B.
#
#
#
# Example 1:
#
#
#
# Input: A = "ab", B = "ba"
# Output: true
#
#
#
# Example 2:
#
#
# Input: A = "ab", B = "ab"
# Output: false
#
#
#
# Example 3:
#
#
# Input: A = "aa", B = "aa"
# Output: true
#
#
#
# Example 4:
#
#
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true
#
#
#
# Example 5:
#
#
# Input: A = "", B = "aa"
# Output: false
#
#
#
#
#
#
#
#
# Constraints:
#
#
# 0 <= A.length <= 20000
# 0 <= B.length <= 20000
# A and B consist only of lowercase letters.
#
#
#

# @lc code=start
from collections import Counter
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
      # Base case: if either string is not present, return False
      if not A or not B:
        return False

      # Base case: if lengths are different, there's no way they can equal each other after swapping
      if len(A) != len(B):
        return False

      if A == B:
        count_A = Counter(A)
        count_B = Counter(B)
        if any([ count_A[letter] >= 2 for letter in count_A]) and any([ count_B[letter] >= 2 for letter in count_B]):
          return True

      pointer = 0
      length = len(A)

      different_count = 0
      indices = []


      while pointer < length:
        if A[pointer] != B[pointer]:
          different_count += 1
          indices.append(pointer)
        pointer += 1

      if different_count == 2:
        if A[indices[0]] == B[indices[1]] and A[indices[1]] == B[indices[0]]:
          return True

      return False


# @lc code=end
