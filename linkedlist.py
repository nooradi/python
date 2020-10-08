class Node:

    def __init__(self, data):
        self.data = data
        self.nextNode = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.numOfNodes = 0

    def insert_end(self, data):

        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.nextNode = new_node
            self.tail = new_node
            self.tail.nextNode = None

    def insert_start(self, data):

        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    def remove_first(self):

        self.numOfNodes = self.numOfNodes - 1

        if self.numOfNodes == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.nextNode

    def remove(self, data):

        self.numOfNodes = self.numOfNodes - 1

        if self.head is None:
            return

        pointer = self.head
        pointer_previous = None

        while pointer is not None and pointer.data != data:
            pointer_previous = pointer
            pointer = pointer.nextNode

        if pointer is None:
            return

        if pointer_previous is None:
            self.head = self.head.nextNode
        else:
            pointer_previous.nextNode = pointer.nextNode

    def size(self):
        return self.numOfNodes

    def traverse(self):

        pointer = self.head

        while pointer is not None:
            print pointer.data
            pointer = pointer.nextNode

