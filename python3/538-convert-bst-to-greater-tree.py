#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Easy (54.86%)
# Likes:    1888
# Dislikes: 115
# Total Accepted:    118.7K
# Total Submissions: 216K
# Testcase Example:  '[5,2,13]'
#
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that
# every key of the original BST is changed to the original key plus sum of all
# keys greater than the original key in BST.
#
# Example:
#
#
# Input: The root of a Binary Search Tree like this:
# ⁠             5
# ⁠           /   \
# ⁠          2     13
#
# Output: The root of a Greater Tree like this:
# ⁠            18
# ⁠           /   \
# ⁠         20     13
#
#
# Note: This question is the same as 1038:
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
#
#

# @lc code=start

# Idea: We can do an inorder tree traversal, perhaps with a recursive DFS.
# We will populate a stack of nodes, from strictly increasing values.
# Then we'll pop the stack, or iterate backwards from the end of the stack,
# and keep a running sum, with which we will add to each popped node's value.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

      # Base Case:
      if not root:
        return None

      # Recursive method that adds to a stack
      def dfs(node, stack):
        # left
        if node.left:
          dfs(node.left, stack)
        # node
        if node:
          stack.append(node)
        # right
        if node.right:
          dfs(node.right, stack)

      stack = []
      dfs(root, stack)
      running_sum = 0
      while stack:
        node = stack.pop()
        if node:
          node.val += running_sum
          running_sum = node.val
      return root


# @lc code=end

# Driver:
root = TreeNode(5, TreeNode(2), TreeNode(13))
print(Solution().convertBST(root))
