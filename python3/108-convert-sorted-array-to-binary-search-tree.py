#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/
#
# algorithms
# Easy (57.20%)
# Likes:    2597
# Dislikes: 220
# Total Accepted:    420.6K
# Total Submissions: 725.9K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given an array where elements are sorted in ascending order, convert it to a
# height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
#
# Example:
#
#
# Given the sorted array: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
#
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
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


# Idea: Naturally, we can take the middle number from the list and make that the root node of tree.
# We can recursively do this, each time, taking the middle value and making that the root of the subtree.
# The values to the left will comprise of the left subtree's value, likewise the right values will be the right subtree.
# If we follow this pattern, we will end up with a tree that is balanced height-wise.
from typing import List
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

      if not nums:
        return None

      mid = len(nums) // 2

      # We're going to recursively build out the subtrees for the left and right
      root = TreeNode(nums[mid])
      root.left = self.sortedArrayToBST(nums[:mid])
      root.right = self.sortedArrayToBST(nums[mid+1:])

      return root


# @lc code=end

