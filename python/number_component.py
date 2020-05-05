"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.



Example 1:

Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.


Example 2:

Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.


Note:

The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
"""
class Solution:
    def findComplement(self, num: int) -> int:

        # 1st, convert the integer into binary:
        quotient = num
        remainders = []
        while quotient > 0:
          remainders.append(quotient % 2)
          quotient = quotient // 2


        # remainders is backwards now, but iterate through, adding up
        # 2nd, iterate each digit and notice that if 0, we add it to the running total
        twos_digit = 0
        output = 0
        for num in remainders:
          if num == 0: # Change this to 1 if you want the correct number
            output += 2 ** twos_digit
          twos_digit += 1

        return output

# Driver
print(Solution().findComplement(5))
print(Solution().findComplement(1))
print(Solution().findComplement(37))