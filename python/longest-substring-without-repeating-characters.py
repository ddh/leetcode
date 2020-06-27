"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

# Idea:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        best_length = 0
        current_length = 0

        last_index = {}
        i = 0

        while i <= len(s):
          if s[i] not in last_index:
            last_index[s[i]] = i
            current_length += 1
          else:
            last_index[char] = i
            i = i + 1
            current_length = i - start_index
          best_length = max(best_length, current_length)


        return best_length





# Driver:
print(Solution().lengthOfLongestSubstring("abcabcbb")) # 3
print(Solution().lengthOfLongestSubstring("bbbbbb")) # 1
print(Solution().lengthOfLongestSubstring("pwwkew")) # 3
print(Solution().lengthOfLongestSubstring("aab")) # 2
print(Solution().lengthOfLongestSubstring("dvdf")) # 3
print(Solution().lengthOfLongestSubstring("tmmzuxt")) # 5