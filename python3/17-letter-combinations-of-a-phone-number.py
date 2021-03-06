#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (46.26%)
# Likes:    3832
# Dislikes: 408
# Total Accepted:    603.3K
# Total Submissions: 1.3M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
#
#
#
# Example:
#
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
#
#
# Note:
#
# Although the above answer is in lexicographical order, your answer could be
# in any order you want.
#
#

# @lc code=start

from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
      phone_mapping = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
      }

      answers = []


      def recurse(output, digits):
        if not digits:
          return answers.append(output)
        else:
          current_digit = digits[0]
          for letter in phone_mapping[current_digit]:
            recurse(output + letter, digits[1:])

      if digits:
        recurse('', digits)

      return answers

# @lc code=end

print(Solution().letterCombinations('23'))