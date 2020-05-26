"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""

# Definition for a binary tree node.
from typing import List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

      # Immediately return if no root
      if not root:
        return None

      visited = []
      level = []
      queue = deque()
      queue.append(root)

      while queue:
        node = queue.popleft()

        if node not in visited:
          # Add node to list of checked nodes
          visited.append(node)
          print(f'Currently looking at node: {node.val}')
          print(f'Visited Nodes so far: {visited}')

          # Append children nodes at the end of queue
          # They will be explored
          if node.left:
            queue.append(node.left)
          if node.right:
            queue.append(node.right)
      for node in visited:
        print(f'{node.val}, ')
      return visited

# Driver:
# [1,2,3,nil,5,nil,4]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
Solution().rightSideView(root)