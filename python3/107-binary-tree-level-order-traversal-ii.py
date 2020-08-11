#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (51.55%)
# Likes:    1553
# Dislikes: 216
# Total Accepted:    360.5K
# Total Submissions: 673.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
#
# return its bottom-up level order traversal as:
#
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
#
#
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Idea: Probably have to use a stack? Maybe an array of nodes? An array of an array of nodes?

from typing import List
from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
      if not root:
        return None

      queue = deque([root])
      results = deque()

      # This is how to BFS, level by level.
      # deque is very useful for this because you can appendleft
      while queue:
        nodes_in_level = len(queue)
        values_in_level = []
        for _ in range(nodes_in_level):
          current = queue.popleft()
          if current:
            values_in_level.append(current.val)
          if current.left:
            queue.append(current.left)
          if current.right:
            queue.append(current.right)
        results.appendleft(values_in_level)

      return results

# @lc code=end

# Driver:
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))) # Sample Data
print(Solution().levelOrderBottom(root))



