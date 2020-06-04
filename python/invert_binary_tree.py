# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Recursive DFS approach
from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
      if root is None: return None
      root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
      return root

# BFS approach:
    def invertTreeBFS(self, root: TreeNode) -> TreeNode:
      if root is None: return None

      queue = deque([root])

      while queue:
        node = queue.popleft()
        node.left, node.right = node.right, node.left
        if node.left:
          queue.append(node.left)
        if node.right:
          queue.append(node.right)
      return root
