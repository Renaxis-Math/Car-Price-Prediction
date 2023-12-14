# ok!
from collections import defaultdict

class newNode:
	def __init__(self, data):
		self.Next = None
		self.child = None
		self.val = data

# Add child Node to a Node
def addChild(n, data):
	
	def addSibling(node):
		if not node: return None

		while (node.Next): node = node.Next
		node.Next = newNode(data)
		
		return node.Next  
	
	if (n == None): return None
 
	if n.child: return addSibling(n.child)
	else:
		n.child = newNode(data)
		return n.child

# Traverses tree in depth first order
def traverseTree(root):
	if (root == None):
		return

	while (root):
		# print(root.val, end = " ")
		if (root.child):
			traverseTree(root.child)
		root = root.Next

def build_lcrs_tree(parents, values):
	nodePos_node_map = {}
	for i in range(len(parents)):
		nodePos_node_map[i] = newNode(node_values[i])

	for i in range(len(parents)):
		node, parent, node_val = i, parents[i], node_values[i]
		
		if parent == -1: continue
		else:
			parent_node = nodePos_node_map[parent]
			new_node = addChild(parent_node, node_val)
			# print(f"n{i} = addChild({parent_node.val}, {node_val})")
			
			nodePos_node_map[i] = new_node
	
	return nodePos_node_map[0]

def max_path_sum(root):
	max_path = -float('inf')

	# post order traversal of subtree rooted at `node`
	def gain_from_subtree(node):
		nonlocal max_path

		if not node: return 0

		# add the gain from the left subtree. Note that if the
		# gain is negative, we can ignore it, or count it as 0.
		# This is the reason we use `max` here.
		gain_from_left = max(gain_from_subtree(node.child), 0)

		gain_from_right = -float('inf')
		# add the gain / path sum from right subtree. 0 if negative
		if node.child:
			gain_from_right = max(gain_from_subtree(node.child.Next), 0)
		
		# if left or right gain are negative, they are counted
		# as 0, so this statement takes care of all four scenarios
		max_path = max(max_path, gain_from_left + gain_from_right + node.val)

		# return the max sum for a path starting at the root of subtree
		return max(
			gain_from_left + node.val,
			gain_from_right + node.val
		)

	gain_from_subtree(root)
	return max_path

parents = [-1, 0, 1, 2, 0]
node_values = [5, 7, -10, 4, 15]
# node_values = [-2, 10, 10, -3, 10]
# node_values = [0, 1, 2, 3, 4]

root = build_lcrs_tree(parents, node_values)
print(max_path_sum(root))