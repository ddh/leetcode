#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#
# https://leetcode.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (50.75%)
# Likes:    1130
# Dislikes: 124
# Total Accepted:    176.7K
# Total Submissions: 347.9K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Find the sum of all left leaves in a given binary tree.
#
# Example:
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
# There are two left leaves in the binary tree, with values 9 and 15
# respectively. Return 24.
#
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
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
      left_leaves = []
      def dfs(node, left, left_leaves):
        if not node:
          return
        if node.left:
          dfs(node.left, True, left_leaves)
        if node.right:
          dfs(node.right, False, left_leaves)
        if not node.left and not node.right:
          if left:
            left_leaves.append(node.val)


      # Base case:
      if not root:
        return 0

      if root.left:
        dfs(root.left, True, left_leaves)
      if root.right:
        dfs(root.right, False, left_leaves)

      return sum(left_leaves)

# @lc code=end

