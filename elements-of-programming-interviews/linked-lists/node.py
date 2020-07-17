class Node:
    def __init__(data = 0, next_node = None):
       self.data = val
       self.next_node = next_node
    
def search(L, k):
    while L and L.data != k:
        L = L.next_node
    return L
    
# Insert a new node after a given node

def insert(L, k, v):
    root = L
    while root:
        if root.value == k:
            new_node = Node(k, root.next_node)
            root.next_node = node
        root = root.next_node
    return L

def delete(L, v):
    while L:
        if L.data == v:

