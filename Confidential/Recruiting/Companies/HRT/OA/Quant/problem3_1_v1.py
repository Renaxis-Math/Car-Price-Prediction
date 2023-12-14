class Node:
    def __init__(self, key, value, children = []):
        self.key = key
        self.val = value
        self.children = children

def solution(arg1):
    nodes = arg1
    seen_children_i = set()
    
    # Build seen_children_i  
    for i, node in enumerate(nodes):
       key, val = node[0], node[1]
       if len(node) == 2: pass
       else:
            children_i = node[1:]
            for child_i in children_i: 
                seen_children_i.add(child_i)
    # \Build seen_children_i
    
    # Build root_i
    root_i = 0
    for i in range(len(nodes)):
        if i not in seen_children_i: 
            root_i = i
            break
    # \Build root_i
    
    # Build tree
    root = None
    seenIndex_nodes = {}
    for i, node_package in enumerate(nodes):
        key, val, children_indices = node_package[0], node_package[1], node_package[2:]
        if i == root_i: 
            root = Node(key, val, children_indices)
            seenIndex_nodes[i] = root
        else:
            cur_node = Node(key, val, children_indices)
            seenIndex_nodes[i] = cur_node        
    # \Build tree
    
    answers = []
    # Traverse tree
    stack = [root]
    while stack:
        nodes_count = len(stack)
        for _ in range(nodes_count):
            cur_node = stack.pop()
            key, val = cur_node.key, cur_node.val
            
            answers.extend([key, val])
            
            children_indices = cur_node.children
            for i in range(len(children_indices) - 1, -1, -1):
                children_i = children_indices[i]
                child_node = seenIndex_nodes[children_i]
                stack.append(child_node)
    # \Traverse tree
    return answers