#
# @lc app=leetcode id=1128 lang=python3
#
# [1128] Number of Equivalent Domino Pairs
#
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/
#
# algorithms
# Easy (47.36%)
# Likes:    199
# Dislikes: 105
# Total Accepted:    22.6K
# Total Submissions: 47.6K
# Testcase Example:  '[[1,2],[2,1],[3,4],[5,6]]'
#
# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] =
# [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is,
# one domino can be rotated to be equal to another domino.
#
# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and
# dominoes[i] is equivalent to dominoes[j].
#
#
# Example 1:
# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
#
#
# Constraints:
#
#
# 1 <= dominoes.length <= 40000
# 1 <= dominoes[i][j] <= 9
#
#

# @lc code=start


# Idea: We'll iterate through each domino, and ensure that the pair of numbers is sorted from least to greatest.
# Then we will put the tuple into a hash, counting it.

from typing import List
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:

      if not dominoes:
        return 0

      counter = {}
      for domino in dominoes:
        if domino[0] > domino[1]:
          domino[0], domino[1] = domino[1], domino[0]
        counter[(domino[0], domino[1])] = counter.get((domino[0], domino[1]), 0) + 1

      return sum([count * (count - 1) // 2 for (_, _), count in counter.items()])

# @lc code=end

print(Solution().numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))
print(Solution().numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6],[1,2]]))
print(Solution().numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6],[1,2],[1,2],[6,5]]))

