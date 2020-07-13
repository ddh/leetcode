#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#
# https://leetcode.com/problems/detect-capital/description/
#
# algorithms
# Easy (53.27%)
# Likes:    475
# Dislikes: 249
# Total Accepted:    111.8K
# Total Submissions: 209.6K
# Testcase Example:  '"USA"'
#
# Given a word, you need to judge whether the usage of capitals in it is right
# or not.
#
# We define the usage of capitals in a word to be right when one of the
# following cases holds:
#
#
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
#
# Otherwise, we define that this word doesn't use capitals in a right way.
#
#
#
# Example 1:
#
#
# Input: "USA"
# Output: True
#
#
#
#
# Example 2:
#
#
# Input: "FlaG"
# Output: False
#
#
#
#
# Note: The input will be a non-empty word consisting of uppercase and
# lowercase latin letters.
#
#

# @lc code=start

# Idea: First detect whether the first letter is capitalized or not.
# Depending on the first letter, if not capitalized, we know the rest of the
# word should be lowercased as well.
# If first letter is capitalized, then scan the rest of the letters and ensure
# the letter's case follows these rules:
# 1. all letters must be lowercased
# 2. Or all letters must be capitalized
# To do these checks, we'll do an equality check against 'a'.
# 1. letter < 'a' means it is capitalized
# 2. letter >= 'a' means it is lower cased
# *. We're assuming a-z,A-Z letters only, latin only
class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        # If < 'a', first letter is capitalized
        if word[0] < 'a':
          # If letter is < 'a', it means it is capitalized
          if all([letter < 'a' for letter in word[1:]]):
            return True
            # If letter is >= 'a', then it is lowercased
          if all([letter >= 'a' for letter in word[1:]]):
            return True
          return False
        else:
          if all([letter >= 'a' for letter in word[1:]]):
            return True
# @lc code=end

print(Solution().detectCapitalUse("USA"))
print(Solution().detectCapitalUse("leetcode"))
print(Solution().detectCapitalUse("Flaf"))
print(Solution().detectCapitalUse("FlaG"))