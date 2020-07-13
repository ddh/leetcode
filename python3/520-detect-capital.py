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
class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        # If < 'a', first letter is capitalized
        if word[0] < 'a':
          if all([letter < 'a' for letter in word[1:]]):
            return True
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