class Node:
    """Node for SingleList"""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SingleList:
    """SingleList class"""

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def insert_tail(self, node):
        if self.length == 0:
            self.head = self.tail = node
        else:  #adding at the tail of list
            self.tail.next = node
            self.tail = node
        self.length += 1

    def remove_head(self):
        if self.length == 0:
            raise ValueError("empty list")
        node = self.head
        if self.head == self.tail:  # self.length == 1
            self.head = self.tail = None
        else:
            self.head = self.head.next
        node.next = None  # clear node.next
        self.length -= 1
        return node.data  # return deleted node

    def sum_q(self):
        node = self.head
        sum = 0
        while node is not None:
            complexity = node.data
            sum += complexity
            node = node.next
        return sum

    def printList(self):
        node = self.head
        while (node):
            print(node.data),
            node = node.next

    def search(self, x, y):
        # Initialize current to head
        current = self.head
        # loop till current not equal to None
        while current != None:
            if current.data >= x and current.data <= y:
                return current.data  # data found /return data
            current = current.next
        return False  # Data Not found /return false

    def deleteNode(self, key):
        # Store head node
        temp = self.head
        # If head node itself holds the key to be deleted
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        # Search for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        # if key was not present in linked list
        if (temp == None):
            return
        # Unlink the node from linked list
        prev.next = temp.next
        temp = None

    def sortList_A(self):
        # Node current will point to head
        current = self.head
        index = None

        if self.head == None:
            return
        else:
            while current != None:
                # Node index will point to node next to current
                index = current.next
                while index != None:
                    # If current node's data is greater than index's node data, swap the data between them
                    if current.data > index.data:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next

    def sortList_D(self):
        # Node current will point to head
        current = self.head
        index = None

        if self.head == None:
            return
        else:
            while current != None:
                # Node index will point to node next to current
                index = current.next

                while index != None:
                    # If current node's data is greater than index's node data, swap the data between them
                    if current.data < index.data:
                        temp = current.data
                        current.data = index.data
                        index.data = temp
                    index = index.next
                current = current.next
