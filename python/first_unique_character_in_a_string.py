"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
      # char_dict = {}
      # for index, char in enumerate(s):
      #   char_dict[char] = char_dict.get(char, 0) + 1
      char_dict = collections.Counter(s)
      for index, char in enumerate(s):
        if char_dict[char] == 1:
          return index
      return -1

import collections
class Solution2:
  def firstUniqChar(self, s: str) -> int:
    letter_counts = defaultdict(lambda a: 0)
    print(letter_counts)




# Driver
print(Solution2().firstUniqChar("leetcode"))
print(Solution2().firstUniqChar("loveleetcode"))
print(Solution2().firstUniqChar(""))
print(Solution2().firstUniqChar("cc"))