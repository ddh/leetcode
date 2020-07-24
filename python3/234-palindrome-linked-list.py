#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (38.91%)
# Likes:    3179
# Dislikes: 359
# Total Accepted:    428.4K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
#
# Example 1:
#
#
# Input: 1->2
# Output: false
#
# Example 2:
#
#
# Input: 1->2->2->1
# Output: true
#
# Follow up:
# Could you do it in O(n) time and O(1) space?
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

      # BC: No nodes
      if not head:
        return False

      # BC: Only one node
      if head.next == None:
        return True

      x

# @lc code=end

