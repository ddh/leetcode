# Largest BST Subtree
# 
# Find the largest BST subtree. A subtree must include all of its descendants.
# Can you figure this out in O(n) complexity?
# Input: [10,5,15,1,8,null,7]
# Output: 3 (size of the largest subtree)

# O(n) complexity:
# You can take advantage of the fact that given [n, n+1, n+2] where n is element 1, n+1 element 2, ...
# n+1 < n < n+2
# So given:
# n, n+1, n+2, n+3, n+4, null, n+5, null, n+6, n+7...etc
#           n
#       n+1   n+2
#     n+3 n+4
#   n+5
# n+6 n+7
# null means to skip to the next available leaf. If there are no leafs on that "level", skip to the next available leaf one level

  class Node
    attr_accessor :left_child, :right_child, :value

    def initialize(value, left_value = nil, right_value = nil)
      @value = value
      @left_child = Node.new(left_value)
      @right_child = Node.new(right_value)
    end
    def to_s
      "value: #{value} left: #{left_child.value} right: #{right_child.value}"
    end
    # TODO: What happens when the values are the same? I dunno.
    def self.valid_bst_node?(node)
      node.left_child.value < node.value && node.right_child.value > node.value
    end
  end


  Node.new(1, 2, 3)

