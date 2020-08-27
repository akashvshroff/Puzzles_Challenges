class Node:
    """
    Builds a node of a tree.
    """

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def in_order_traversal(root):
    """
    Traverses a binary tree in the in-order form using an iterative approach as
    compared to the usual recursive approach.
    """
    cur = root
    stack = []
    while True:
        if cur is not None:
            stack.append(cur)
            cur = cur.left
        elif stack:
            cur = stack.pop()
            print(cur.data, end=" ")
            cur = cur.right
        else:
            break
    print()


def main():
    """
    Driver program to test the in-order traversal.
    """
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)
    in_order_traversal(root)


if __name__ == '__main__':
    main()
