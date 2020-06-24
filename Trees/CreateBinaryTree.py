class Node:
    def __init__ (self, data):
        self.data =  data
        self.left = None
        self.right = None

def inorder(root):
    if (not root):
        return

    inorder(root.left)
    print(root.data, end = " ")
    inorder(root.right)

def preorder(root):
    if (not root):
        return

    print(root.data, end = " ")
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if (not root):
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end = " ")

def insert(node, data):
    my_queue = []
    my_queue.append(node)

    while(len(my_queue) != 0):

        front = my_queue[0]
        my_queue.pop(0)

        if front.left == None:
            front.left = Node(data)
            break
        else:
            my_queue.append(front.left)

        if front.right == None:
            front.right = Node(data)
            break
        else:
            my_queue.append(front.right)

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)

    print("Inorder traversal")
    inorder(root)

    print("\nPreorder traversal")
    preorder(root)

    print("\nPostorder traversal")
    postorder(root)

    insert(root, 35)
    print("\nPreorder traversal after inserting")
    preorder(root)
