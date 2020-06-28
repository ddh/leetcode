#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#
# https://leetcode.com/problems/keyboard-row/description/
#
# algorithms
# Easy (64.44%)
# Likes:    533
# Dislikes: 649
# Total Accepted:    110.3K
# Total Submissions: 171.2K
# Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
#
# Given a List of words, return the words that can be typed using letters of
# alphabet on only one row's of American keyboard like the image below.
#
#
#
#
#
#
# Example:
#
#
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
#
#
#
#
# Note:
#
#
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.
#
#
#

# @lc code=start

# Ideas: This is a simple dictionary-type problem. We'll create a three dictionaries,
# one for each row of the keyboard. Then we'll iterate through each of the words and
# iterate through the letters of each word, checking to see if they are all contained
# in any of the three dictionaries.

# Time complexities:
# O(3n) -> O(n) to create the letter-row dictionaries
# if m = num of words and p = num of letters per word
# O(m*p)

# Be sure to downcase the words

from typing import List
class Solution:
    def findWords(self, words: List[str]) -> List[str]:

      qwertyuiop_set = set('qwertyuiop')
      asdfghjkl_set = set('asdfghjkl')
      zxcvbnm_set = set('zxcvbnm')

      answers = []

      # A little redundant but it works
      for word in words:
        if all([letter in qwertyuiop_set for letter in word.lower()]):
          answers.append(word)
        if all([letter in asdfghjkl_set for letter in word.lower()]):
          answers.append(word)
        if all ([letter in zxcvbnm_set for letter in word.lower()]):
          answers.append(word)
      return answers

# @lc code=end

print(Solution().findWords(['Hello', 'Alaska', 'Dad', 'Peace']))
