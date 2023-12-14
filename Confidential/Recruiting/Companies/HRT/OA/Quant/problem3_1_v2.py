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

def f(arg1):
    nodes = arg1
    root = build_tree(nodes)
    answers = preOrder_traverse(root)
    return answers

arg1 = [[4,3], 
 [1,15,3,2,0], 
 [1,0,4], 
 [6,3], 
 [2,3]]
assert f(arg1) == [1, 15, 6, 3, 1, 0, 2, 3, 4, 3]

arg1 = [[5,6], 
 [5,6,0]]
assert f(arg1) == [5, 6, 5, 6]

arg1 = [[5427,4527,3,4,2], 
 [5155,3684,0], 
 [270,877], 
 [5621,1104], 
 [9814,6901], 
 [5460,5587,1]]
assert f(arg1) == [5460, 5587, 5155, 3684, 5427, 4527, 5621, 1104, 9814, 6901, 270, 877]

arg1 = [[5604,5022]]
assert f(arg1) == [5604, 5022]

arg1 = [[9417,4424,1], 
 [2873,3937,4], 
 [673,8427], 
 [6119,9716,5], 
 [9241,8561,9], 
 [8552,1055,0], 
 [245,9624,2], 
 [1929,3610,8], 
 [1463,1156,6], 
 [9071,7102,7]]
assert f(arg1) == [6119, 9716, 8552, 1055, 9417, 4424, 2873, 3937, 9241, 8561, 9071, 7102, 1929, 3610, 1463, 1156, 245, 9624, 673, 8427]

arg1 = [[7786,9023,6,3,4,2,1,5,7,8], 
 [5234,6320], 
 [8553,8303], 
 [437,6945], 
 [3014,7697], 
 [3291,9875], 
 [1910,7997], 
 [1338,6122], 
 [6137,6521]]
assert f(arg1) == [7786, 9023, 1910, 7997, 437, 6945, 3014, 7697, 8553, 8303, 5234, 6320, 3291, 9875, 1338, 6122, 6137, 6521]