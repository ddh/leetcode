"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.



Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation:
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation:
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.


Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.
"""

from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        good_words = []

        usable_chars_dict = {}
        for char in chars:
          usable_chars_dict[char] = usable_chars_dict.get(char, 0) + 1

        for word in words:
          available_chars = usable_chars_dict.copy()
          rejected = None
          for char in word:
            if char in available_chars and available_chars[char] > 0:
              available_chars[char] -= 1
            else:
              rejected = True
              break
          if not rejected: good_words.append(word)

        return len(''.join(good_words))


# Driver:
print(Solution().countCharacters(["cat","bt","hat","tree"], "atach"))