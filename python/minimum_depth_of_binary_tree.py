"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""

# Idea: We want the minimum depth. That sounds like shortest path to me. What we'll do is BFS and stop as soon as a leaf child is detected.
# We BFS unti we reach the first leaf. Then we return the depth. We'll need to keep track of the depth


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:

      if not root:
        return 0
      if not root.left and not root.right:
        return 1


      queue = deque()
      queue.append(root)
      depth = 1

      while queue:
        node_count_for_level = len(queue)
        for _ in range(node_count_for_level):
          node = queue.popleft()
          if not node.left and not node.right:
            return depth
          if node.left:
            queue.append(node.left)
          if node.right:
            queue.append(node.right)
        depth += 1

# Driver
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().minDepth(root)) # min depth = 2
print(Solution().minDepth(TreeNode(1))) # just the root, 1
print(Solution().minDepth(None)) # No tree, 0