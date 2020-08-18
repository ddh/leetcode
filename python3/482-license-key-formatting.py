#
# @lc app=leetcode id=482 lang=python3
#
# [482] License Key Formatting
#
# https://leetcode.com/problems/license-key-formatting/description/
#
# algorithms
# Easy (43.05%)
# Likes:    467
# Dislikes: 738
# Total Accepted:    131.3K
# Total Submissions: 304.7K
# Testcase Example:  '"5F3Z-2e-9-w"\n4'
#
# You are given a license key represented as a string S which consists only
# alphanumeric character and dashes. The string is separated into N+1 groups by
# N dashes.
#
# Given a number K, we would want to reformat the strings such that each group
# contains exactly K characters, except for the first group which could be
# shorter than K, but still must contain at least one character. Furthermore,
# there must be a dash inserted between two groups and all lowercase letters
# should be converted to uppercase.
#
# Given a non-empty string S and a number K, format the string according to the
# rules described above.
#
# Example 1:
#
# Input: S = "5F3Z-2e-9-w", K = 4
#
# Output: "5F3Z-2E9W"
#
# Explanation: The string S has been split into two parts, each part has 4
# characters.
# Note that the two extra dashes are not needed and can be removed.
#
#
#
#
# Example 2:
#
# Input: S = "2-5g-3-J", K = 2
#
# Output: "2-5G-3J"
#
# Explanation: The string S has been split into three parts, each part has 2
# characters except the first part as it could be shorter as mentioned
# above.
#
#
#
# Note:
#
# The length of string S will not exceed 12,000, and K is a positive integer.
# String S consists only of alphanumerical characters (a-z and/or A-Z and/or
# 0-9) and dashes(-).
# String S is non-empty.
#
#
#

# @lc code=start
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:

      def get_only_letters(string: str):
        return string.replace('-', '')

      def capitalize_letters(string: str):
        return string.upper()

      S = get_only_letters(capitalize_letters(S))

      # Base case: When
      if len(S) <= K:
        return S

      num_of_groups = len(S) // K
      remainder = len(S) % K

      # Create array in advance of correct length of answer
      answer = ([''] * (num_of_groups * K)) + ([''] * (num_of_groups - 1))
      if remainder > 0:
        answer += [''] * remainder # For the first remainder letters
        answer += [''] # For the first dash

      answer_pointer = 0
      letter_pointer = 0
      letter_length = len(S)

      # If there was a remainder, take care of printing the first group of letters
      # Because we take care of the base case above when string is less than K,
      # We need not worry about the fence-post at the end. There will always one
      # because at this point, there will always be more than K values.
      if remainder > 0:

        for i, letter in enumerate(S[:remainder]):
          answer[i] = letter
          answer_pointer += 1
          letter_pointer += 1
        answer[answer_pointer] = '-'
        answer_pointer += 1

      # Now take care of the rest of the groups
      for _ in range(num_of_groups):
        for _ in range(K):
          answer[answer_pointer] = S[letter_pointer]
          answer_pointer += 1
          letter_pointer += 1
        if letter_pointer < letter_length:
          answer[answer_pointer] = '-'
          answer_pointer += 1

      return ''.join(answer)
# @lc code=end

print(Solution().licenseKeyFormatting("5F3Z-2e-9-w", 4))