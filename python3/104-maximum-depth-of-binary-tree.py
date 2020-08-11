#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (65.47%)
# Likes:    2597
# Dislikes: 75
# Total Accepted:    840.9K
# Total Submissions: 1.3M
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given binary tree [3,9,20,null,null,15,7],
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# return its depth = 3.
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Idea: We can do a simple dfs, comparing the depth from left child or right child
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

      if not root:
        return 0

      def dfs(node, depth):
        if node:
          depth += 1
          return max(dfs(node.left, depth), dfs(node.right, depth))
        if not node:
          return depth

      return dfs(root, 0)
# @lc code=end

