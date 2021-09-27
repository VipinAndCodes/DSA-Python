
class Node:

    def __init__(self):
        self.data = data
        self.nextNode = None


# O(1) running complixity
class LinkedList:

    def __init__(self):
        self.head = None
        self.numOfNodes = 0

    def insert_start(self,data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.nextNode = self.head
            self.head = new_node

    def insert_end(self,data):
        self.numOfNodes = self.numOfNodes + 1
        new_node = Node(data)
#actual ndde last node of linked list
        actual_node = self.head

    while actual_node.nextNode is not None:
        actual_node = actual_node.nextNode

    actual_node.nextNode = new_node

#NEED



