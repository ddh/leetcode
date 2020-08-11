#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#
# https://leetcode.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (46.50%)
# Likes:    4247
# Dislikes: 104
# Total Accepted:    665.6K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# Given a binary tree, check whether it is a mirror of itself (ie, symmetric
# around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
#
#
#
#
# But the following [1,2,2,null,3,null,3] is not:
#
#
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
#
#
#
#
# Follow up: Solve it both recursively and iteratively.
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List
from collections import deque
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

      level = deque()
      level.append(root)

      while level:

        # Check if the level is symmetric
        level_values = []
        level_count = len(level)

        # Build the next level, also storing values of next level
        for _ in range(level_count):
          node = level.popleft()
          if node:
            level.append(node.right)
            level.append(node.left)
            level_values.append(node.val)
          else:
            level_values.append(None)

        # print(level_values) # Debug
        head_ptr, tail_ptr = 0, len(level_values) - 1
        while head_ptr < tail_ptr:
          if level_values[head_ptr] != level_values[tail_ptr]:
            return False
          else:
            head_ptr += 1
            tail_ptr -= 1
      return True

# @lc code=end

