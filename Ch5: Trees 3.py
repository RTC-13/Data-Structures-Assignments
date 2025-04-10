class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None

# Get input
def get_input_tree():
    root = None
    print("Enter your tree then type exit when done.")
    while True:
        inp = input("num or exit: ")
        if inp == 'exit':
            break
        try:
            # make it a number
            inp = int(inp)
            # insert into the tree
            root = insert_bst(root, inp)
        except ValueError:
            print("Please enter a valid number")
    return root

# insert
def insert_bst(root, value):
    if root is None:
        return Node(value)
    if value < root.data:
        root.left = insert_bst(root.left, value)
    else:
        root.right = insert_bst(root.right, value)
    return root

def find_kth_largest(root, k):
    elements = []
    def reverse_inorder(node):
        
        if node:
            reverse_inorder(node.right)
            elements.append(node.data)
            reverse_inorder(node.left)
    reverse_inorder(root)
    if k > 0 and k <= len(elements):
        return elements[k - 1]
    return None

def sum_greater_equal(root, k_largest):
    total_sum = 0
    def inorder_check(node):
        # this lets me change the outer variable without giving me errors (thanks google)
        nonlocal total_sum 
        if node:
            inorder_check(node.left)
            if node.data >= k_largest:
                total_sum += node.data
            inorder_check(node.right)
    inorder_check(root)
    return total_sum

def print_tree(root):
    vals = []
    def inorder_print(node):
        if node:
            inorder_print(node.left)
            vals.append(str(node.data))
            inorder_print(node.right)
    inorder_print(root)
    print("Tree values (sorted hopefully):", ", ".join(vals))

if __name__ == "__main__":
    my_tree = get_input_tree()

    if my_tree:
        print_tree(my_tree)

        k_value = int(input("Please enter K (NUM): "))
        kth_large = find_kth_largest(my_tree, k_value)

        if kth_large is not None:
            the_sum = sum_greater_equal(my_tree, kth_large)
            print(f"\nThe {k_value}th largest number is: {kth_large}")
            print(f"Sum of numbers bigger or equal to {k_value}: {the_sum}")
        else:
            print(f"Couldn't find the {k_value}th largest (probably not enough numbers in the provided treee.).")
    else:
        print("No tree.")