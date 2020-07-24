#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (36.77%)
# Likes:    1111
# Dislikes: 151
# Total Accepted:    189.4K
# Total Submissions: 513.5K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
#
# Example 1:
#
#
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
#
# Example 2:
#
#
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
#
# Example 3:
#
#
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
#
# Example 4:
#
#
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
#
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters that may be separated by a single space.
#
#

# @lc code=start

# Idea: Need to split up the pattern into letters first.
# Each letter must correlate to a word
# No letter can map to several words
# No word can map to several letters.
# Use a dictionary

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
      words = str.split()

      # Base case: lengths don't match:
      if len(words) != len(pattern):
        return False

      i = 0
      mappings = {}
      letters_explored = set()

      for i in range(len(words)):
        # print(f'Looking at word: {words[i]} and letter {pattern[i]}')
        if words[i] not in mappings:
          if pattern[i] not in letters_explored:
            mappings[words[i]] = pattern[i]
            letters_explored.add(pattern[i])
          else:
            return False
        # The word is found in the mappings,
        # So check what letter it is. Is it the same as the one
        # we are currently on in the `pattern`?
        else:
          if mappings[words[i]] != pattern[i]:
            return False

      return True

# @lc code=end

print(Solution().wordPattern("abba", "dog cat cat dog"))
print(Solution().wordPattern("abba", "dog cat cat fish"))

