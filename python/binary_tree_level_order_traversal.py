"""Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

      # Base case: There is no root, so no tree.
      if not root:
        return None

      # Let's keep track of the nodes we'll iterate through with a queue
      queue = deque()
      # Then prime the queue with the first node, which is the root
      queue.append(root)
      # We will keep a list of the answers
      results = []


      while queue:
        num_nodes_for_level = len(queue)

        # Keep track of this level's values
        level_values = []
        for _ in range(num_nodes_for_level):
          node = queue.popleft()
          level_values.append(node.val)

          if node.left:
            queue.append(node.left)
          if node.right:
            queue.append(node.right)

        results.append(level_values)

      return results



# Driver:
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().levelOrder(root))
