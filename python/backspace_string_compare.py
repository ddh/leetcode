"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_s, stack_t = [], []
        for char in S:
          stack_s.pop() if char == '#' and stack_s else stack_s.append(char)
        for char in T:
          stack_t.pop() if char == '#' and stack_t else stack_t.append(char)
        print(stack_s)
        print(stack_t)
        return stack_s == stack_t

# Driver
print(Solution().backspaceCompare("ab##", "c#d#"))
print(Solution().backspaceCompare("y#fo##f", "y#f#o##f"))