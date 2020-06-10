"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Idea:
# For iteratively, we'll load each node in the array. Then we'll iterate from both ends of the array towards the middle, swapping VALUES as we go along.
# This is kind of cheating since this takes advantage that the only difference between the nodes are its values.
#
# For Recursive: TBD
#
# Explanation from Gayle (cracking code): https://www.youtube.com/watch?v=njTh_OwMljA

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Uses a stack. Looks straightforward
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

      # Base case:
      if not head:
        return None

      # Create a list of nodes
      nodes = []
      while head:
        nodes.append(head)
        head = head.next

      head_pointer = 0
      tail_pointer = len(nodes) - 1

      while head_pointer < tail_pointer:
        nodes[head_pointer].val, nodes[tail_pointer].val = nodes[tail_pointer].val, nodes[head_pointer].val
        head_pointer += 1
        tail_pointer -= 1

      return nodes[0] # return head node

# Another way to iterate, swapping nodes and not the values. More proper in case nodes are complicated to swap data.
# This is a little confusing to me because of the temporary node in the while loop.
class Solution2:
  def reverseList(self, head: ListNode) -> ListNode:
    # Base case:
    if not head:
      return None

    previous_node = None
    current_node = head

    while current_node:
      temp_node = current_node
      current_node = current_node.next
      temp_node.next = previous_node
      previous_node = temp_node
    return previous_node

# I don't the recursive one. I translated the following from a java recursive solution.
# Besides, it's hard to comprehend from first glance. Iterative is easier to understand!
class Solution3:
  def reverseList(self, head: ListNode) -> ListNode:
    if not head or head.next is None:
      return head
    node = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return node

# Driver
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

Solution().reverseList(a)
Solution2().reverseList(a)