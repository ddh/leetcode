"""
Given a binary tree, find the leftmost value in the last row of the tree.

Example 1:
Input:

    2
   / \
  1   3

Output:
1
Example 2:
Input:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

Output:
7
Note: You may assume the tree (i.e., the given root node) is not NULL.
"""

from typing import List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:

      # Base case: No root, no tree
      if not root:
        return None
      # Iterate through the nodes using a queue
      queue = deque()
      queue.append(root)

      level_values = []
      while queue:
        num_of_nodes_in_level = len(queue)

        for _ in range(num_of_nodes_in_level):
          node = queue.popleft()
          level_values.append(node.val)
          if node.right:
            queue.append(node.right)
          if node.left:
            queue.append(node.left)


      return level_values[-1] # Nonsense return value


# Driver
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)
print(Solution().findBottomLeftValue(root)) # 7
