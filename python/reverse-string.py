"""
https://leetcode.com/problems/reverse-string/
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.
"""


from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        front, back = 0, len(s) - 1
        while front < back:
          s[front], s[back] = s[back], s[front]
          front += 1
          back -= 1
        return ''.join(s)



class Solution2:
    def reverseString(self, s: List[str]) -> None:
        head_pointer = 0
        tail_pointer = len(s) - 1

        num_of_swaps = len(s) // 2

        for _ in range(num_of_swaps):
          s[head_pointer], s[tail_pointer] = s[tail_pointer], s[head_pointer]
          head_pointer += 1
          tail_pointer -= 1

        return s


print(Solution2().reverseString(["h","e","l","l","o"])) # ["o","l","l","e","h"]
