#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (43.91%)
# Likes:    713
# Dislikes: 1165
# Total Accepted:    226.7K
# Total Submissions: 513.1K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
#
# Example 1:
#
#
# Input: "hello"
# Output: "holle"
#
#
#
# Example 2:
#
#
# Input: "leetcode"
# Output: "leotcede"
#
#
# Note:
# The vowels does not include the letter "y".
#
#
#
#

# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
      vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] # Remember to add the capitalized

      result = []
      vowels_only = []

      for letter in s:
        if letter in vowels:
          vowels_only.append(letter)
          result.append(None)
        else:
          result.append(letter)

      pointer = 0
      for letter in vowels_only[::-1]:
        while result[pointer] != None:
          pointer += 1
        result[pointer] = letter

      return ''.join(result)

# @lc code=end

