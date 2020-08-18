#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#
# https://leetcode.com/problems/path-sum-iii/description/
#
# algorithms
# Easy (45.77%)
# Likes:    3954
# Dislikes: 304
# Total Accepted:    216K
# Total Submissions: 457.4K
# Testcase Example:  '[10,5,-3,3,2,null,11,3,-2,null,1]\n8'
#
# You are given a binary tree in which each node contains an integer value.
#
# Find the number of paths that sum to a given value.
#
# The path does not need to start or end at the root or a leaf, but it must go
# downwards
# (traveling only from parent nodes to child nodes).
#
# The tree has no more than 1,000 nodes and the values are in the range
# -1,000,000 to 1,000,000.
#
# Example:
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
# ⁠     10
# ⁠    /  \
# ⁠   5   -3
# ⁠  / \    \
# ⁠ 3   2   11
# ⁠/ \   \
# 3  -2   1
#
# Return 3. The paths that sum to 8 are:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3. -3 -> 11
#
#
#

# Idea: We'll do a DFS recursive call. The idea here is to do a post-order traversal:
# Look left, right, then process the node. Each node should return an array of sums,
# which includes the sums from left, right and self. Add self's value to each of the values
# from the left and right children.
# Along the way, we keep track of the number of times we've encountered the sum.

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:


      self.count = 0
      def dfs(self, node):
        if not node:
          return

        sums = [node.val]
        if node.left:
          left_sums = dfs(self, node.left)
          for branch_sum in left_sums:
            sums.append(node.val + branch_sum)

        if node.right:
          right_sums = dfs(self, node.right)
          for branch_sum in right_sums:
            sums.append(node.val + branch_sum)

        for num in sums:
          if num == sum:
            self.count += 1
        return sums

      dfs(self, root)
      return self.count


# @lc code=end

# Summary:
# We should only visit each node once, so O(n) time complexity?

root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))
print(Solution().pathSum(root, 8))