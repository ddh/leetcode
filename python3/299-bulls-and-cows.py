#
# @lc app=leetcode id=299 lang=python3
#
# [299] Bulls and Cows
#
# https://leetcode.com/problems/bulls-and-cows/description/
#
# algorithms
# Easy (42.14%)
# Likes:    671
# Dislikes: 810
# Total Accepted:    159.7K
# Total Submissions: 376.6K
# Testcase Example:  '"1807"\n"7810"'
#
# You are playing the following Bulls and Cows game with your friend: You write
# down a number and ask your friend to guess what the number is. Each time your
# friend makes a guess, you provide a hint that indicates how many digits in
# said guess match your secret number exactly in both digit and position
# (called "bulls") and how many digits match the secret number but locate in
# the wrong position (called "cows"). Your friend will use successive guesses
# and hints to eventually derive the secret number.
#
# Write a function to return a hint according to the secret number and friend's
# guess, use A to indicate the bulls and B to indicate the cows. 
#
# Please note that both secret number and friend's guess may contain duplicate
# digits.
#
# Example 1:
#
#
# Input: secret = "1807", guess = "7810"
#
# Output: "1A3B"
#
# Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
#
# Example 2:
#
#
# Input: secret = "1123", guess = "0111"
#
# Output: "1A1B"
#
# Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a
# cow.
#
# Note: You may assume that the secret number and your friend's guess only
# contain digits, and their lengths are always equal.
#

# Idea: We'll count the frequency of letters first from the secret.
# We then keep track of num bulls, cows. We iterate through the guessed number.
# Each time we

# @lc code=start
from collections import Counter
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
      secret = str(secret)
      guess = str(guess)

      bulls, cows = 0, 0

      letter_frequency = Counter(secret)

      for i, num in enumerate(guess):
        if num in letter_frequency:
          if num == secret[i]:
            bulls += 1
            if letter_frequency[num] <= 0: cows -= 1 # This conditional is tricky unless you work out an example
          else:
            if letter_frequency[num] > 0: cows += 1 # This conditional is tricky unless you work out an example
          letter_frequency[num] -= 1

      return str(bulls) + "A" + str(cows) + "B"




# @lc code=end

print(Solution().getHint("1807", "7810")) # 1A3B
print(Solution().getHint("1123", "0111")) # 1A1B
print(Solution().getHint("1122", "1222")) # 3A0B
print(Solution().getHint("6244988279", "3819888600")) # 2A2B