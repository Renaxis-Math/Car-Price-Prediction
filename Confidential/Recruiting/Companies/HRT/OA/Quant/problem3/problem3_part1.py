from typing import Optional

class Node:
    def __init__(self, *, key: int = -1, value: int = -1) -> None:
        self.key = key
        self.value = value
        self.child_nodes = []
        self.parent_node = None
        return
        
    def add_child_node(self, child_node: 'Node') -> None: # Forward Reference Technique
        self.child_nodes.append(child_node)
        return
    
    def get_child_nodes(self) -> list['Node']:
        return [child_node for child_node in self.child_nodes]
    
    def set_parent_node(self, node: 'Node') -> None:
        self.parent_node = node
        return
    
class Tree:
    def __init__(self, nodeIndex_node_map: dict = {}) -> None:
        self.root_index = self._find_root_index(nodeIndex_node_map)
        self.root_node = nodeIndex_node_map[self.root_index] if self.root_index != -1 else None
        return
        
    def _find_root_index(self, nodeIndex_node_map: dict) -> int:
        for i, node in nodeIndex_node_map.items():
            if node.parent_node is None: return i
        return -1
    
    def debug(self, nodeIndex_node_map) -> None:
        if isinstance(nodeIndex_node_map, dict):
            for i, node in nodeIndex_node_map.items():
                print(f"Node {i}:")
                print(node.key, node.value)
                print(f"Children = {node.child_nodes}")
                print(f"Parent = {node.parent_node}")
        print(f"Root index is {self.root_index}")
        return
    
    def get_root_node(self) -> 'Node':
        return self.root_node
    
def build_nodeIndex_node_map(nodes_list: list[list[int]]) -> dict:
    nodeIndex_node_map = {i: Node(key=nodes_list[i][0], value=nodes_list[i][1]) 
                        for i in range(len(nodes_list))}

    for node_index, node in nodeIndex_node_map.items():
        _, _, *child_indices = nodes_list[node_index]
        for child_index in child_indices:
            child_node = nodeIndex_node_map[child_index]
            
            child_node.set_parent_node(node)
            node.add_child_node(child_node)
    
    return nodeIndex_node_map

def preOrder_traversal(answers: list, node: Optional['Node'] = None) -> None:
    if node is None: return
    answers.extend([node.key, node.value])
    for child_node in node.child_nodes:
        preOrder_traversal(answers, child_node)
    return

def f(nodes_list: list[list[int]]) -> list[int]:
    nodeIndex_node_map = build_nodeIndex_node_map(nodes_list)
    tree = Tree(nodeIndex_node_map)
    # tree.debug(nodeIndex_node_map)
    
    answers = []
    preOrder_traversal(answers, tree.root_node)
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
