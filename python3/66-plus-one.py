#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (42.20%)
# Likes:    1466
# Dislikes: 2333
# Total Accepted:    593.1K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
#
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
#
# Example 1:
#
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#
#
# Example 2:
#
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#
#

# @lc code=start

# Idea: The tricky part here is if we encounter a 9 anywhere in the list of digits. Encountering
# a '9' will require us to 'carry the one', which can be tricky if have several '9's in a row.
# EG: [9,9] will be [1,0,0].
# Take note that we don't have to deal with negative numbers.
from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

      # Base case: empty list
      if not digits:
        return None

      # Base case: for number zero
      if len(digits) == 0:
        return [1]

      # Else:
      answerArray = []
      counter = 0
      carry = True
      while counter < len(digits):
        current_number = digits[-(counter+1)]
        if carry:
          current_number += 1
          if current_number == 10:
            answerArray.append(0)
          else:
            answerArray.append(current_number)
            carry = False
        else:
          answerArray.append(current_number)
        counter +=1

      # If we're still left with a carryover, tack on a 1 at the very end.
      if carry:
        answerArray.append(1)

    # return answerArray[::-1]

      # Now reverse the answer array to get the final answer
      answerArray.reverse()
      return answerArray

# Driver:
print(Solution().plusOne([1,2,3]))
print(Solution().plusOne([1,2,9]))
print(Solution().plusOne([9]))
print(Solution().plusOne([9,9,9]))

# @lc code=end

