"""
Given the root of a binary search tree with distinct values, modify it so that every node has a new value equal to the sum of the values of the original tree that are greater than or equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.



Example 1:

Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]



Constraints:

    The number of nodes in the tree is between 1 and 100.
    Each node will have value between 0 and 100.
    The given tree is a binary search tree.

Note: This question is the same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

      # In-order traversal using dfs.
      # The key here is to add the nodes visited to a stack.
      def dfs(self, node: TreeNode):
        if node.left:
          dfs(self, node.left)
        if node:
          self.stack.append(node)
        if node.right:
          dfs(self, node.right)

      self.stack = []
      incremental_sum = 0
      dfs(self, root)

      # We'll then pop the stack (node with largest val on top)
      while self.stack:
        node = self.stack.pop()
        incremental_sum += node.val
        node.val = incremental_sum

      return root



root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

Solution().bstToGst(root)
