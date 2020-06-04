"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]



Note:

    S string length is in [1, 10000].
    C is a single character, and guaranteed to be in string S.
    All letters in S and C are lowercase.

"""

# IDea: We're going to iterate through the array forward, then backwards.
# As we're going through the array, we'll increment a counter that will represent
# how many elements we've gone since last seeing the target element.
# Once we hit the target element, we'll stop and iterate backwards, setting
# a new answer's array to the value - i, which is where we found the element.
# Continue to do this for the rest and then do it backwards.
# Then take the min from the forwards vs backwards for final answer.

from typing import List
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:

      forward_array = [0] * len(S)
      backward_array = [0] * len(S)

      target_index = -1
      steps = 0

      for i, letter in enumerate(S):
        forward_array[i] = steps
        if letter == C:
          target_index = i
          steps = 0
        steps += 1
      print(forward_array)
      return [0]

# Driver:
print(Solution().shortestToChar("loveleetcode", "e"))