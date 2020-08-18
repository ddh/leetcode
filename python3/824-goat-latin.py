#
# @lc app=leetcode id=824 lang=python3
#
# [824] Goat Latin
#
# https://leetcode.com/problems/goat-latin/description/
#
# algorithms
# Easy (62.98%)
# Likes:    323
# Dislikes: 650
# Total Accepted:    69K
# Total Submissions: 108.8K
# Testcase Example:  '"I speak Goat Latin"'
#
# A sentence S is given, composed of words separated by spaces. Each word
# consists of lowercase and uppercase letters only.
#
# We would like to convert the sentence to "Goat Latin" (a made-up language
# similar to Pig Latin.)
#
# The rules of Goat Latin are as follows:
#
#
# If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of
# the word.
# For example, the word 'apple' becomes 'applema'.
#
# If a word begins with a consonant (i.e. not a vowel), remove the first letter
# and append it to the end, then add "ma".
# For example, the word "goat" becomes "oatgma".
#
# Add one letter 'a' to the end of each word per its word index in the
# sentence, starting with 1.
# For example, the first word gets "a" added to the end, the second word gets
# "aa" added to the end and so on.
#
#
# Return the final sentence representing the conversion from S to Goat
# Latin. 
#
#
#
# Example 1:
#
#
# Input: "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
#
#
# Example 2:
#
#
# Input: "The quick brown fox jumped over the lazy dog"
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa
# hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
#
#
#
#
# Notes:
#
#
# S contains only uppercase, lowercase and spaces. Exactly one space between
# each word.
# 1 <= S.length <= 150.
#
#
#

# Idea: This just tests your algo organization.

# @lc code=start
class Solution:
    def toGoatLatin(self, S: str) -> str:
      vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

      words = S.split(' ')

      answers = []

      for i, word in enumerate(words):
        if word[0] not in vowels:
          word = word[1:] + word[0]
        answers.append(word + "ma" + ("a" * (i + 1)))

      return ' '.join(answers)

# @lc code=end

print(Solution().toGoatLatin("I speak goat latin"))
a = "a"
a += ("A" * 3)
print(a)