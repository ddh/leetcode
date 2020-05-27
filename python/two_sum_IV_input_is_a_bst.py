"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True


Example 2:

Input:
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""

# Idea: BFS. When processing a node, check to see if its complement exists in a set.
# If not, then we add the value to the set, hoping that the next node processed will
# pair up with a number in the set, to add up to target value


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
      complements = set()
      queue = deque()
      queue.append(root)

      while queue:
        node = queue.popleft()
        if node:
          # Process node:
          if k - node.val in complements:
            return True
          else:
            complements.add(node.val)

          if node.left:
            queue.append(node.left)
          if node.right:
            queue.append(node.right)
      return False


# Driver:
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)
print(Solution().findTarget(root, 9)) # True
print(Solution().findTarget(root, 28       )) # True