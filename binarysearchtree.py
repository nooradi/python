class Node:

    def __init__(self, data, parent):
        self.data = data
        self.rightChild = None
        self.leftChild = None
        self.parent = parent


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):

        if not self.root:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, root):

        new_node = Node(data, root)

        if root.data <= data:
            if root.rightChild:
                self.insert_node(data, root.rightChild)
            else:
                root.rightChild = new_node
        else:
            if root.leftChild:
                self.insert_node(data, root.leftChild)
            else:
                root.leftChild = new_node

    def traverse_postorder(self):
        if self.root:
            self.traverse_postorder_helper(self.root)

    def traverse_postorder_helper(self, root):

        if root.leftChild:
            self.traverse_postorder_helper(root.leftChild)

        if root.rightChild:
            self.traverse_postorder_helper(root.rightChild)

        if root:
            print root.data

    def traverse_preorder(self):
        if self.root:
            self.traverse_preorder_helper(self.root)

    def traverse_preorder_helper(self, root):

        if root:
            print root.data

        if root.leftChild:
            self.traverse_preorder_helper(root.leftChild)

        if root.rightChild:
            self.traverse_preorder_helper(root.rightChild)

    def traverse_inorder(self):
        if self.root:
            self.traverse_inorder_helper(self.root)

    def traverse_inorder_helper(self, root):

        if root.leftChild:
            self.traverse_inorder_helper(root.leftChild)

        print root.data

        if root.rightChild:
            self.traverse_inorder_helper(root.rightChild)

    def get_max(self):
        pointer = self.root
        while pointer is not None:
            if not pointer.rightChild:
                print pointer.data
            pointer = pointer.rightChild

    def get_min(self):
        pointer = self.root
        while pointer is not None:
            if not pointer.leftChild:
                print pointer.data
            pointer = pointer.leftChild

