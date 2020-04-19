"""
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).



Example 1:

Input: num = 9669
Output: 9969
Explanation:
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.


Constraints:

1 <= num <= 10^4
num's digits are 6 or 9.
"""

"""
Notes:
* 666 = len(666) = 3
change 0th place, add 300. 3 * 10 * 10, len(666) - (index + 1)
change index-1, 696, add 30, 3 * 10 ^ 2, len(666) - (index + 1)
change index-2, 669, add 3, 3 * 10 ^ 0, len(666) - (index + 1)
"""
class Solution:
    def maximum69Number (self, num: int) -> int:
      stringified = str(num)
      count = 0
      for digit in stringified:
        if digit == '9':
          count += 1
        else:
          break

      if count == len(stringified): return num
      return num + 3 * 10 ** (len(stringified) - count - 1)

# Sweet one-liner
class Solution2:
   def maximum69Number(self, num):
        return int(str(num).replace('6', '9', 1))

# Driver
print(Solution().maximum69Number(9669))