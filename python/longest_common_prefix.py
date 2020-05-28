"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""

# Idea: We can scan the first letter of all strings and ensure they are the same. Then we increment the prefix with that
# letter if they're the same. Then move on to the next one.
# At worst, all strings are the same of length S, and we hit each letter * # of strings

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
      prefix = ""

      # Some base cases
      if not strs:
        return prefix
      if len(strs) == 1:
        return strs[0]

      # Finding out the shortest word in the list. This will be the max potential length of prefix
      max_prefix_length = min(len(word) for word in strs)
      i = 0

      while i < max_prefix_length:
        letter_count = set() # Keeping track of the letters encountered
        for word in strs:
          letter_count.add(word[i])

        # If there was only one letter in the set, we know all strings had that same letter!
        if len(letter_count) == 1:
          prefix += letter_count.pop()
          i += 1
        else:
          return prefix
      return prefix

# Driver:
# print(Solution().longestCommonPrefix(None)) # ""
# print(Solution().longestCommonPrefix([])) # "fl"
print(Solution().longestCommonPrefix(["flower","flow","flight"])) # "fl"
print(Solution().longestCommonPrefix(["dog","racecar","car"])) # "", no common prefix
print(Solution().longestCommonPrefix(["apple","applejacks","appletree","appletini"])) # "", no common prefix