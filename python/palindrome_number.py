"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true

Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:

Coud you solve it without converting the integer to a string?
"""

# Idea:

# Source Code:
class Solution:
    def isPalindrome(self, x: int) -> bool:
      # Base case; negative numbers are not palindromic
      if x < 0:
        return False

      # Base case; single digit numbers are always palindromic
      if x % 10 == x:
        return True

      # Base case; number ends in a 0, it is not palindromic
      if x % 10 == 0:
        return False

      # Helper method that returns the nth digit starting from the right, 0-indexed
      def nth_digit(number, digit_from_right):
        return int(number * 10 ** -digit_from_right) % 10

      # Helper method that returns number of digits for a number
      def len_of_number(number):
        original_number = number
        counter = 0
        divisor = 1
        while number % divisor != original_number:
          counter += 1
          divisor *= 10
        return counter

      # Create array of digits for x
      digits = [nth_digit(x, i) for i in range(len_of_number(x))]

      # Check for equality in reversed list
      return digits == digits[::-1]

# Driver:
print(Solution().isPalindrome(121)) # True, 121
print(Solution().isPalindrome(-121)) # False, 121-
print(Solution().isPalindrome(10)) # False, 01
print(Solution().isPalindrome(9)) # True, 9
print(Solution().isPalindrome(0)) # True, 0
print(Solution().isPalindrome(8888)) # True, 9