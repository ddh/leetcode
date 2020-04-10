"""
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.



Example 1:

Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"
Example 2:

Input: "aeiou"
Output: ""
"""
class Solution:
    def removeVowels(self, S: str) -> str:
      return ''.join([letter for letter in S if letter not in ['a', 'e', 'i', 'o', 'u']])
