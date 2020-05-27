"""
938. Range Sum of BST
Easy

1051

190

Add to List

Share
Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.



Example 1:

Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
Example 2:

Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
Output: 23


Note:

The number of nodes in the tree is at most 10000.
The final answer is guaranteed to be less than 2^31.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive DFS does not use a stack. Sum must be a class variable though
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:

      self.sum = 0

      # Recursive DFS
      def dfs(node):
        if node:
          if L <= node.val <= R:
            self.sum += node.val
          if node.left:
            dfs(node.left)
          if node.right:
            dfs(node.right)
      dfs(root)
      return self.sum

# Iterative DFS uses a stack
class Solution2:
  def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    sum = 0
    stack = [root]

    while stack:
      node = stack.pop()
      if node:
          if L <= node.val <= R:
            sum += node.val
          if node.left:
            stack.append(node.left)
          if node.right:
            stack.append(node.right)

    return sum

# Driver:
# root = TreeNode(10)

# Solution().rangeSumBST(root)

