"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.
"""

# This needs improvement. Hard to read

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
      alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
      s_list = list(S)
      front_pointer, last_pointer = 0, len(S) - 1
      while front_pointer < last_pointer:
        while s_list[front_pointer] not in alphabet:
          front_pointer += 1
          break
        while s_list[last_pointer] not in alphabet:
          last_pointer -= 1
          break
        if s_list[front_pointer] in alphabet and s_list[last_pointer] in alphabet:
          s_list[front_pointer], s_list[last_pointer] = s_list[last_pointer], s_list[front_pointer]
          front_pointer += 1
          last_pointer -= 1

      return ''.join(s_list)


# Driver:
print(Solution().reverseOnlyLetters("j-Ih-gfE-dCba")) # "a-bC-dEf-ghIj"
print(Solution().reverseOnlyLetters("7_28]")) # "a-bC-dEf-ghIj"