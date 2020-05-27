"""
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""

# Idea: We know a palindrome has matching letters at opposite ends. Except if it's an odd number string, it will have the one letter in the middle.
# So what we'll do is just store a count of the letters in a hashtable
# But we'll have to keep track of the number of odd letters with a counter. Everytime we add to the hash table, if the value is already there,
# we'll increment this 'odds' counter. If the element is not there, we decrease the odds counter by one. In the end, if the odds counter is
# greater than 1, we know that there are too many characters that don't have a pair bc at most we can have the one odd in the middle of the sequence.

from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
      odds_counter = 0
      counts = Counter()

      for letter in s:
        if counts[letter] % 2 == 1:
          odds_counter -= 1
        else:
          odds_counter += 1
        counts[letter] += 1
      return odds_counter <= 1





# Driver:
print(Solution().canPermutePalindrome("code")) # False
print(Solution().canPermutePalindrome("aab")) # True
print(Solution().canPermutePalindrome("carerac")) # True