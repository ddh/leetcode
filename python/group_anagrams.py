"""
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      anagrams = defaultdict(list)
      for word in strs:
        anagrams[''.join(sorted(word))].append(word)
      return list(anagrams.values())


# Driver
print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))