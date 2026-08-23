class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value

def insert(root,value):
    if root is None:
        return Node(value)
    if root.data == value:
        return root
    if root.data > value:
        root.left = insert(root.left,value)
    else:
        root.right = insert(root.right,value)
    return root

def search(root,value):
    if root is None:
        print("\nElement Not Found",end = "\n")
        return
    if root.data == value:
        print("Element Found")
        return
    if root.data > value:
        search(root.left,value)
    else:
        search(root.right,value)

def get_successor(root):
    root = root.right
    while root is not None and root.left is not None:
        root = root.left
    return root #it will return inorder successor

def delete(root,value):
    if root is None:
        return root
    if root.data > value:
        root.left = delete(root.left, value)
    elif root.data < value:
        root.right = delete(root.right, value)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            succ = get_successor(root)
            root.data = succ.data
            root.right = delete(root.right,succ.data)
    return root

def InOrder(root):
    if root is not None:
        InOrder(root.left)
        print(root.data, end=" ")
        InOrder(root.right)


root = insert(None,20)
root = insert(root, 15)
root = insert(root, 12)
root = insert(root,18)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 50)
root = insert(root, 25)
# root = Node(20)
# root.left = Node(15)
# root.left.left = Node(12)
# root.left.right = Node(18)
# root.right = Node(30)
# root.right.right = Node(40)

InOrder(root)
search(root,16)
search(root,12)
search(root,30)

delete(root,30)
# print("\n")
InOrder(root)
