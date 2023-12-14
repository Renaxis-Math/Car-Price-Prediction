class Node:
    def __init__(self, key, value, children = []):
        self.key = key
        self.val = value
        self.children = children
        
def find_root_i(nodes):
    seen_children_i = set()

    for i, node in enumerate(nodes):
        key, val = node[0], node[1]
        if len(node) == 2: continue
        else: seen_children_i.update(node[1:])
                
    root_i = 0
    for i in range(len(nodes)):
        if i not in seen_children_i: return i
            
    return root_i

def build_tree(nodes):
    seenIndex_nodes = {}
    root_i = find_root_i(nodes)

    for i, node_package in enumerate(nodes):
        key, val, children_indices = node_package[0], node_package[1], node_package[2:]
        if i == root_i: 
            root = Node(key, val, children_indices)
            seenIndex_nodes[i] = root
        else:
            cur_node = Node(key, val, children_indices)
            seenIndex_nodes[i] = cur_node
            
    for i in range(len(nodes)):
        cur_node = seenIndex_nodes[i]
        cur_children_indices = cur_node.children

        for j in range(len(cur_children_indices) - 1, -1, -1):
            cur_children_i = cur_children_indices[j]
            child_node = seenIndex_nodes[cur_children_i]
            cur_node.children[j] = child_node
        
        seenIndex_nodes[i] = cur_node        
    
    root = seenIndex_nodes[root_i]
    return root
    
def merge_trees(left, right):
    if left.key != right.key:
        return None

    merged_node = Node(left.key, right.val)
    merged_children = {}

    for child in left.children + right.children:
        if child.key in merged_children:
            merged_children[child.key] = merge_trees(merged_children[child.key], child)
        else:
            merged_children[child.key] = child

    merged_node.children = list(merged_children.values())
    return merged_node

def preOrder_traverse(root):
    answers = []
    stack = [root]
    
    while stack:
        nodes_count = len(stack)
        for _ in range(nodes_count):
            cur_node = stack.pop()
            key, val = cur_node.key, cur_node.val
            
            answers.extend([key, val])

            for child in cur_node.children[::-1]:
                stack.append(child)

    return answers         

def solution(left, right):
    left_root = build_tree(left)
    right_root = build_tree(right)
    
    if left_root.key != right_root.key: return []
    
    merged_root = merge_trees(left_root, right_root)
    answer = preOrder_traverse(merged_root)
    
    return answer