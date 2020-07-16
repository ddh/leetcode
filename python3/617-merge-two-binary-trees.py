#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#
# https://leetcode.com/problems/merge-two-binary-trees/description/
#
# algorithms
# Easy (73.73%)
# Likes:    3057
# Dislikes: 172
# Total Accepted:    299.3K
# Total Submissions: 405K
# Testcase Example:  '[1,3,2,5]\n[2,1,3,null,4,null,7]'
#
# Given two binary trees and imagine that when you put one of them to cover the
# other, some nodes of the two trees are overlapped while the others are not.
#
# You need to merge them into a new binary tree. The merge rule is that if two
# nodes overlap, then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of new tree.
#
# Example 1:
#
#
# Input:
# Tree 1                     Tree 2
# ⁠         1                         2
# ⁠        / \                       / \
# ⁠       3   2                     1   3
# ⁠      /                           \   \
# ⁠     5                             4   7
# Output:
# Merged tree:
# 3
# / \
# 4   5
# / \   \
# 5   4   7
#
#
#
#
# Note: The merging process must start from the root nodes of both trees.
#
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        # Base cases where a root not present.
        # Just return the present one.
        if not t1:
         return t2 if t2 else None
        if not t2:
          return t1 if t1 else None

        # Else, we dfs the two trees in tandem:
        # Here, we can assume node1 and node2 are not null,
        # and will have a value. Whether or not they have a
        # left or right will determine if we recurse further
        #
        # When either node1 or node2 does not have a left/right,
        # we'll stop recursing.
        #
        # If it is node1 that doesn't have the child but node2 does,
        # We'll need to add node2's child to node1 since we are
        # modifying in reference to node1
        def dfs(node1, node2):
          if node1.left and node2.left:
            dfs(node1.left, node2.left)

          if not node1.left and node2.left:
            node1.left = node2.left

          node1.val += node2.val

          if node1.right and node2.right:
            dfs(node1.right, node2.right)

          if not node1.right and node2.right:
            node1.right = node2.right

        dfs(t1, t2)

        return t1
# @lc code=end

