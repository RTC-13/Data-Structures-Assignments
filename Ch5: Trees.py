class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

#1 Function to insert a new node using Preorder DFS
def insertPreorder(root, value):
    # if there is no value return the root as a new node.
    if root is None:
        return Node(value)

    # Check if we can insert at the same level as node 3
    if root.left is None:
        root.left = Node(value)  # Insert as the left 
    elif root.right is None:
        root.right = Node(value)  # Insert as the right 
    else:
        # If left and right, recursively call on left.
        insertPreorder(root.left, value)

    return root

#2 Postorder function
def printPostorder(node):
    if node is None:
        return
    
    # Left subtree
    printPostorder(node.left)

    # Right subtree
    printPostorder(node.right)

    # Deal with the node itself 
    print(node.data, end=" ")

if __name__ == "__main__":
    # Constructing the initial binary tree
    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)

    # 1 Inserting node with value 6 using Preorder DFS (current-left-right)
    root = insertPreorder(root, 6)

    #  2 Displaying Postorder traversal (left-right-currrent)
    print("Postorder traversal: ", end="")
    printPostorder(root)
