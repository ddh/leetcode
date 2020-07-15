#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (53.37%)
# Likes:    842
# Dislikes: 66
# Total Accepted:    88.9K
# Total Submissions: 166K
# Testcase Example:  '[1,null,3,2]'
#
# Given a binary search tree with non-negative values, find the minimum
# absolute difference between values of any two nodes.
#
# Example:
#
#
# Input:
#
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
#
# Output:
# 1
#
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1
# (or between 2 and 3).
#
#
#
#
# Note:
#
#
# There are at least two nodes in this BST.
# This question is the same as 783:
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
#
#
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Idea: We can do an in-order traversal with the numbers into an array.
# Then we'll iterate through the array and keep track of the best minimum
# absolute distance.
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
      # Base case:
      if not root:
        return None

      in_order_traversal = []
      def dfs(node, in_order_traversal):
          if node.left:
            dfs(node.left, in_order_traversal)
          if node:
            in_order_traversal.append(node.val)
          if node.right:
            dfs(node.right, in_order_traversal)

      # DFS to get the in-order traversal
      dfs(root, in_order_traversal)

      min_absolute_difference = float('infinity')

      for i, _ in enumerate(in_order_traversal[:-1]):
        min_absolute_difference = min(min_absolute_difference, abs(in_order_traversal[i] - in_order_traversal[i+1]))

      return min_absolute_difference
# @lc code=end

root = TreeNode(1, None, TreeNode(3, TreeNode(2)))
Solution().getMinimumDifference(root)
