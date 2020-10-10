class AVLTree:

    def __init__(self):
        self.root = None

    class Node:

        def __init__(self, data):
            self.data = data
            self.rightChild = None
            self.leftChild = None
            self.height = 0

    def insert(self, data):
        self.root = self.__insert(data, self.root)

    def __insert(self, data, root):

        new_node = self.Node(data)

        if not root:
            return new_node

        if data < root.data:
            root.leftChild = self.__insert(data, root.leftChild)
        else:
            root.rightChild = self.__insert(data, root.rightChild)

        self.__set_height(root)
        return self.__handle_violation(root)

    def __handle_violation(self, root):

        if self.__left_heavy(root):
            if self.__balance(root.leftChild) < 0:
                root.leftChild = self.__rotate_left(root.leftChild)

            return self.__rotate_right(root)

        elif self.__right_heavy(root):
            if self.__balance(root.rightChild) > 0:
                root.rightChild = self.__rotate_right(root.rightChild)

            return self.__rotate_left(root)

        return root

    def __rotate_left(self, root):

        new_root = root.rightChild

        root.rightChild = new_root.leftChild
        new_root.leftChild = root

        self.__set_height(root)
        self.__set_height(new_root)

        return new_root

    def __rotate_right(self, root):

        new_root = root.leftChild

        root.leftChild = new_root.rightChild
        new_root.rightChild = root

        self.__set_height(root)
        self.__set_height(new_root)

        return new_root

    def __height(self, root):
        if not root:
            return -1

        return root.height

    def __balance(self, root):
        if not root:
            return 0

        return self.__balance_factor(root)

    def __balance_factor(self, node):
        if not node:
            return 0

        return self.__height(node.leftChild) - self.__height(node.rightChild)

    def __left_heavy(self, node):
        return self.__balance_factor(node) > 1

    def __right_heavy(self, node):
        return self.__balance_factor(node) < -1

    def __set_height(self, node):
        node.height = max(self.__height(node.leftChild), self.__height(node.rightChild)) + 1

    def traverse_inorder(self):
        if self.root:
            self.__traverse_inorder(self.root)

    def __traverse_inorder(self, root):

        if root.leftChild:
            self.__traverse_inorder(root.leftChild)

        print root.data

        if root.rightChild:
            self.__traverse_inorder(root.rightChild)

    def traverse_postorder(self):
        if self.root:
            self.__traverse_postorder(self.root)

    def __traverse_postorder(self, root):

        if root.leftChild:
            self.__traverse_postorder(root.leftChild)

        if root.rightChild:
            self.__traverse_postorder(root.rightChild)

        if root:
            print root.data

    def traverse_preorder(self):
        if self.root:
            self.__traverse_preorder(self.root)

    def __traverse_preorder(self, root):

        if root:
            print root.data

        if root.leftChild:
            self.__traverse_preorder(root.leftChild)

        if root.rightChild:
            self.__traverse_preorder(root.rightChild)

