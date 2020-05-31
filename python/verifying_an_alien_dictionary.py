"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""

# Idea: We can look at two words of a time, and in each word, we will compare the letter of each against the alien-alphabet/
# There are a lot of edge cases. For example, same words given, words with similar first few letters, different length words, etc.

from typing import List
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

      # Base case: one word, is already sorted
      if len(words) == 1:
        return True

      # Iterate through each pair of words
      for i, word in enumerate(words[:-1]):
        letter_pointer = 0

        # Iterate through each letter:
        word = words[i]
        other_word = words[i+1]

        for _ in range(min(len(word), len(other_word))):
          same_prefix = word[letter_pointer] == other_word[letter_pointer]
          if order.index(word[letter_pointer]) > order.index(other_word[letter_pointer]):
            return False
          elif order.index(word[letter_pointer]) == order.index(other_word[letter_pointer]):
            same_prefix = True
            letter_pointer += 1
            continue
          else:
            break
        if same_prefix:
          return len(word) < len(other_word)
      return True

# Driver:
print(Solution().isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")) # False
print(Solution().isAlienSorted(["apple"], "abcdefghijklmnopqrstuvwxyz")) # True
print(Solution().isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz")) # False
print(Solution().isAlienSorted(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")) # True
print(Solution().isAlienSorted(["kuvp","q"], "ngxlkthsjuoqcpavbfdermiywz")) # True