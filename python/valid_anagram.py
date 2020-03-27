"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      return sorted(s) == sorted(t) # Cheating

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
      char_count = {}
      for char in s: char_count[char] = char_count.get(char, 0) + 1
      for char in t: char_count[char] = char_count.get(char, 0) - 1
      return False not in [char_count[char] == 0 for char in char_count]




# Driver
print(Solution2().isAnagram("rat", "car"))
print(Solution2().isAnagram("anagram", "nagaram"))