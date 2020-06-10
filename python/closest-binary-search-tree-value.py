"""
https://leetcode.com/problems/closest-binary-search-tree-value/

Closest Binary Search Tree Value
Easy

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

    Given target value is a floating point.
    You are guaranteed to have only one unique value in the BST that is closest to the target.

Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4

"""

# Idea: We will traverse the tree until we get find a value that is larger than the target. Once we hit that large value, we'll traverse its left child (which is smaller)
# and check if it is still larger than the target. If it is still larger than the target, we update that value and continue until the left child is smaller than the target.
# At this point in time, we then traverse dfs all the way down to the right side of the smaller target to find the next largest number after the previous value.
# We will take the number then that is closer to the target value, by taking absolute difference and comparing.

# Another way to approach and think about this is to do an in-order traversal. This gives you from smallest to larget. To optimize, we can immediately stop traversal one we hit a number
# that is larger than the target. From there, we know that the target is in between the last two elements in the in-order traversal.
# We then take whichever is closer in absolute difference.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:

      # Base case:
      if not root:
        return None

      # Base case:
      if root.left is None and root.right is None:
        return root.val

      self.in_order_values = []

      def in_order_dfs(self, node):
        if node.left:
          in_order_dfs(self, node.left)
        value = node.val
        self.in_order_values.append(value)
        if node.right:
          in_order_dfs(self, node.right)

      # Building our in-order traversal
      in_order_dfs(self, root)

      # Iterate through, stopping when current value is larger than tarfget
      for i, value in enumerate(self.in_order_values):
        if value >= target:
          if abs(value - target) <= abs(self.in_order_values[i-1] - target):
            return value
          else:
            return self.in_order_values[i-1]




# Driver:
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(Solution().closestValue(root, 3.714286)) # 4