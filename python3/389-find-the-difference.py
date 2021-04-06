#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#
# https://leetcode.com/problems/find-the-difference/description/
#
# algorithms
# Easy (54.97%)
# Likes:    843
# Dislikes: 285
# Total Accepted:    200.8K
# Total Submissions: 363.1K
# Testcase Example:  '"abcd"\n"abcde"'
#
#
# Given two strings s and t which consist of only lowercase letters.
#
# String t is generated by random shuffling string s and then add one more
# letter at a random position.
#
# Find the letter that was added in t.
#
# Example:
#
# Input:
# s = "abcd"
# t = "abcde"
#
# Output:
# e
#
# Explanation:
# 'e' is the letter that was added.
#
#

# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
      ptr = 0

      # Let's sort the strings and then compare them later.
      # This will take O(2logn) -> O(logn) time to sort
      s = sorted(s)
      t = sorted(t)

      # Make it so that `s` is always shorter, thus the extra letter is always in variable `t`
      if len(t) < len(s):
        s, t = t, s

      # We'll iterate through once, taking O(n)
      while ptr < min(len(s), len(t)):
        if s[ptr] != t[ptr]:
          if t[ptr + 1] == s[ptr]:
            return t[ptr]
          else:
            return s[ptr]
        ptr += 1

      # If we've reached here, we know the missing letter is at the very end of the longer string, which is `t`
      return t[-1]


# @lc code=end

print(Solution().findTheDifference("abcde", "abcd"))
print(Solution().findTheDifference("abcde", "dcba"))
print(Solution().findTheDifference("ae", "aea"))