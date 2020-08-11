#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (62.64%)
# Likes:    3244
# Dislikes: 135
# Total Accepted:    749.6K
# Total Submissions: 1.2M
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# Output: [1,3,2]
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
      stack = []
      # recursive solution
      def dfs(node, stack):
        if not node:
          return stack
        else:
          dfs(node.left, stack)
          stack.append(node.val)
          dfs(node.right, stack)
        return stack

      return dfs(root, stack)

# Iterative:
from collections import deque
class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
      stack = deque(root)

      node = root

      while True:
        if node:
          if node.left:
            node = node.left



# @lc code=end

