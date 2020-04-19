"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
      opens, stars = [], []
      for i, char in enumerate(s):
        if char == "(":
          opens.append(i)
        elif char == "*":
          stars.append(i)
        else:
          if opens: opens.pop()
          elif stars: stars.pop()
          else: return False

      # At this point, we have exhausted all the close parenthesis
      # Now for whatever open parenthesis we have, we'll
      while opens and stars:

        # We're checking if the last record star's position was to the right of the last recorded open.
        # It'll mean we can use the star to close off the open parenthesis
        if stars[-1] > opens[-1]:
          stars.pop()
          opens.pop()
        else:
          break
      return len(opens) == 0

      # Wow, if we've paired off all our opens with any remaining stars, there should be no opens.
      # Any leftover opens means an invalid string.)


# Driver
print(Solution().checkValidString("()")) # True
print(Solution().checkValidString("(*)")) # True
print(Solution().checkValidString("(*))")) # True
print(Solution().checkValidString(")(")) # False
print(Solution().checkValidString("*")) # True
print(Solution().checkValidString("**")) # True
print(Solution().checkValidString("***)")) # True
print(Solution().checkValidString("*(")) # False
print(Solution().checkValidString("()()")) # False