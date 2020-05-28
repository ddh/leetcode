"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""

# Idea: Keep track of two indexes, one for encountering the first word, the other for the second word.
# We then iterate through the array just once, updating the index of each word we encounter.
# Whenever we encounter the word, we see if the currently held shortest_distance is better, then store it.
# Time complexity should be O(n) as we iterate through the list of words just the one time. O(1) space, no additional space created.

from typing import List
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
      # Keep track of the indexes where we find word1, word2
      word1_index = -1
      word2_index = -1
      shortest_distance = len(words) - 1 # The max distance if words were at both ends of the list

      for i, word in enumerate(words):
        if word == word1:
          word1_index = i
          if word2_index >= 0:
            shortest_distance = min(abs(word1_index - word2_index), shortest_distance)
        if word == word2:
          word2_index = i
          if word1_index >= 0:
            shortest_distance = min(abs(word1_index - word2_index), shortest_distance)
      return shortest_distance

# Driver:
print(Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice")) # 3
print(Solution().shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding")) # 1