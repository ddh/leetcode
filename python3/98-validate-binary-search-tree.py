#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (27.59%)
# Likes:    3907
# Dislikes: 536
# Total Accepted:    697.8K
# Total Submissions: 2.5M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
#
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
#
#
# Example 1:
#
#
# ⁠   2
# ⁠  / \
# ⁠ 1   3
#
# Input: [2,1,3]
# Output: true
#
#
# Example 2:
#
#
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
#
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
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
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
      if not root:
        return True


      self.in_order_traversal = []

      # 1. In order bst traversal
      def dfs(self, node):
        if node.left:
          dfs(self, node.left)

        self.in_order_traversal.append(node.val)

        if node.right:
          dfs(self, node.right)


      # 2. invoke dfs on root
      dfs(self, root)

      # 3. Check if the bst is strictly increasing
      for i, _ in enumerate(self.in_order_traversal[:-1]):
        if self.in_order_traversal[i] >= self.in_order_traversal[i + 1]:
          return False
      return True



# @lc code=end

Solution().isValidBST(TreeNode(2, TreeNode(1), TreeNode(3)))