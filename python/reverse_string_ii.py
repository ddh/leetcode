"""
https://leetcode.com/problems/reverse-string-ii/

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Restrictions:

    The string consists of lower English letters only.
    Length of the given string and k will in the range [1, 10000]

"""

# Idea:

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
      self.answer = [char for char in s]

      swap_count = 0
      pointer = 0
      skip = False

      def swap(self, start, end):
        while start < end:
          self.answer[start], self.answer[end] = self.answer[end], self.answer[start]
          end -= 1
          start += 1

      for _ in range(len(s)):
        print("hi")
        if pointer >= len(s):
          break
        if skip:
          pointer += k
          skip = False
        if len(s) - pointer <= k:
          swap(self,pointer, pointer + k)
          skip = True
          pointer += k




      return self.answer


# Driver:
print(Solution().reverseStr("abcdefg", 5)) # "bacdfeg"