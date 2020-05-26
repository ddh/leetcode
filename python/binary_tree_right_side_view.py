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

      # Base case there is no root to begin with
      if not root:
        return None

      # Create the queue, adding nodes level by level
      queue = deque()

      # Prime the queue with the first root
      queue.append(root)

      # Init the answer array. Each element is the furthest right value of each level
      rightmost_values = []

      while queue:

        # Keep track of the number of nodes per level:
        node_count_per_level = len(queue)

        # A list of values for a particular level.
        # We'll want to return the last element at the end
        current_levels_node_values = []

        # The key to this is to iterate through the queue,
        # only though the number of nodes on the level at a time
        for _ in range(node_count_per_level): # customary to use _ if you're not using it whilst iterating
          node = queue.popleft()
          current_levels_node_values.append(node.val)

          # Append children nodes at the end of queue
          if node.left:
            queue.append(node.left)
          if node.right:
            queue.append(node.right)

        # Now that we've iterated through each of the level's node,
        # Take the last value from the level's array of values
        # and append it to the array that we'll return for the answer
        rightmost_values.append(current_levels_node_values[-1])

      return rightmost_values

# Driver:
# [1,2,3,nil,5,nil,4] => 1,3,4
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
print(Solution().rightSideView(root))

# [1,2,3,5,nil,4,nil,nil,6] => 1,3,4,6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
root.left.left.right = TreeNode(6)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
print(Solution().rightSideView(root))