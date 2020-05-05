"""
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)



Example 1:

Input: [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]



Note:

1 <= preorder.length <= 100
The values of preorder are distinct.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from typing import List
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
      # Empty list
      if not preorder:
        return None

      # Set root to first node from list and push to stack
      root = TreeNode(preorder[0])
      stack = [root]

      # Iterate through the rest of the elements
      for num in preorder[1:]:
        current_node = stack[-1]
        next_node = TreeNode(num)

        # If the next node is larger than previous value
        while stack and next_node.val > stack[-1].val:
          current_node = stack.pop()

        # Insert next node to left if smaller than current node
        if next_node.val < current_node.val:
          current_node.left = next_node
        else: # and insert to right if larger
          current_node.right = next_node

        # Finally, remember to
        stack.append(next_node)

      # All done! Return root node:
      return root

print(Solution().bstFromPreorder([8,5,1,7,10,12]))