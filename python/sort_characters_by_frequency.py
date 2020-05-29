"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

# Idea: Be careful with String operations since String is an immutable object.
# Let's count turn the string into an array, then count the frequency.
# We then pull each key by frequency
# We create append an array if each letter

from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:

      counts = Counter(s) # O(n). Inserting each letter in hashmap is O(1) operation
      answer = []

      # We iterate through the counts, with the most frequent letters first
      for letter, frequency in counts.most_common(): # O(nlogn) for sorting by frequency
        for _ in range(frequency): # O(n) as we iterate and insert into answer
          answer.append(letter)

      return "".join(answer) # O(n)

# Driver:
print(Solution().frequencySort("cccaaa")) #  "cccaaa"
