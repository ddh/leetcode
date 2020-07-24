#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (52.27%)
# Likes:    3459
# Dislikes: 124
# Total Accepted:    306.3K
# Total Submissions: 581.7K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
#
# Example:
#
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#
#
# Constraints:
#
#
# 1 <= n <= 19
#
#
#

# @lc code=start

# IDea: This looks like a DP problem; we want to get all possible
# combinations of structurally different BST's.
class Solution:
    def numTrees(self, n: int) -> int:

      # DP # DP # DP # DP
      self.cache = { 0: 1 } # Don't need {1: 1}
      # DP # DP # DP # DP

      def recurse(self, n):

        if n in self.cache:
          return self.cache[n]

        num = 0
        for i in range(1, n + 1):
          left = recurse(self, i-1)
          right = recurse(self, n-i)
          num += left * right

        # DP # DP # DP # DP
        self.cache[n] = num
        # DP # DP # DP # DP

        return num

      return recurse(self,n)


# @lc code=end

print(Solution().numTrees(3))
print(Solution().numTrees(4))
print(Solution().numTrees(5))
