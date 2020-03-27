# 598. N-ary tree Preorder Traversal
class Node
  attr_accessor :value, :children

  def initialize(value)
    @value = value
    @children = []
  end

  def add_child(node)
    @children.append(node)
  end
end

def create_node(value)
  Node.new(value)
end

def add_child(parent_node, child_node)
  parent_node.children.append(child_node)
end

def find_next_child_in_line(parent, child)
  parent.children[parent.children.index(child.value) + 1]
end

# Here's the input, each group of children delimited by nil. Two nil means to move down a layer.
root = [1,nil,2,3,4,5,nil,nil,6,7,nil,8,nil,9,10,nil,nil,11,nil,12,nil,13,nil,nil,14]

# Create a node for each value in original input array
grandparent = nil
parent = nil
first_child = nil
previous_node = nil
new_layer_count = 0 # if 1, add to parent, if 2, parent is first in array of children of current parent
nodes = root.map do |value|

  #
  # if new_layer_count == 2
  #   parent = find_next_child_in_line(grandparent, parent)
  # end

  # Create nodes for known values
  if value
    node = Node.new(value)
    previous_node = node
    new_layer_count = 0
  else
    new_layer_count += 1
  end

  #
  if parent.present?
    parent.add_child(node) unless value
  else
    parent = node
  end

  if new_layer_count == 2

  end

end

current_pointer = nodes[0]
nodes.each do |node|
  next if node == current_pointer
  current_pointer.add_child(node) if current
end