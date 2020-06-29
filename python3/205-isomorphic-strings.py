#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (39.57%)
# Likes:    1358
# Dislikes: 353
# Total Accepted:    290.6K
# Total Submissions: 734.3K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
#
# Example 1:
#
#
# Input: s = "egg", t = "add"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "foo", t = "bar"
# Output: false
#
# Example 3:
#
#
# Input: s = "paper", t = "title"
# Output: true
#
# Note:
# You may assume both s and t have the same length.
#
#

# @lc code=start

# Idea: Nice that we can assume the two strings are of the same length.
# The rule about isomorphic is interesting. Some interesting rules to observe:
# 1. A letter can be mapped to itself. Basically a no-op
# 2. Letters cannot be mapped more than once. Meaning, if there were
# two 'a's in the original string, in the new string, one 'a' cannot be
# mapped to 'b' and the other 'a' cannot be mapped to 'c'. Both 'a's have to
# be mapped to the same character.
# Rule #2 gives us a hint at how we can solve this:
# we can iterate through both words at the same time.
# and keep a map of the first word to the second
# if ever we encounter where the second word's letter maps to
# the first word's letter, but is a differnet latter, we say false.
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

      # Base case: len == 0
      if len(s) == 0:
        return True

      mapping = {}
      mapping_complement = {}
      for i, _ in enumerate(s):
        if s[i] not in mapping:
          if t[i] in mapping_complement and mapping_complement[t[i]] != s[i]:
            return False
          else:
            mapping[s[i]] = t[i]
            mapping_complement[t[i]] = s[i]
        else:
          if mapping[s[i]] != t[i]:
            return False

      return True

# @lc code=end

print(Solution().isIsomorphic('paper', 'title'))
print(Solution().isIsomorphic('aa', 'ab'))
print(Solution().isIsomorphic('bar', 'foo'))

# Thoughts:
# Kinda convoluted code. A little messy.
# My idea here was to keep a mapping of the words, but I
# had to keep a mapping from the other direction also
# There might be a better way to implement this...