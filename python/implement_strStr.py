"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

      # Base cases:
      if needle == "":
        return 0


      haystack_pointer = 0
      needle_pointer = 0
      matched_count = 0

      haystack_length = len(haystack)

      while haystack_pointer < len(haystack):
        if haystack[haystack_pointer] != needle[needle_pointer]:
          haystack_pointer = haystack_pointer - matched_count + 1 # Start at the next element from where we initially started to match the needle
          matched_count = 0
          needle_pointer = 0
        else:
          matched_count += 1
          haystack_pointer += 1
          needle_pointer += 1
        if matched_count == len(needle):
          return haystack_pointer - matched_count
      return -1


# Driver:
print(Solution().strStr("hello", "ll")) # 2