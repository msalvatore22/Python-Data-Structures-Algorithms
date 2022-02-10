from multiprocessing.sharedctypes import Value
from xml.dom import INDEX_SIZE_ERR


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    # same functionality as addAt
    def insert(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                i = 0
                while i < location -1:
                    tempNode = tempNode.next
                    i += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail=newNode
        self.length += 1
    # same functionality as insert
    def addAt(self, value, index):
        node = Node(value)
        currNode = self.head
        prevNode = None
        currIndex = 0

        if index > self.length:
            return False
        
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            if index == 0:
                node.next = currNode
                self.head = node
            elif index == self.length-1:
                node.next = None
                self.tail.next = node
                self.tail = node
            else:
                while currIndex < index:
                    currIndex += 1
                    prevNode=currNode
                    currNode=currNode.next

                node.next = currNode
                prevNode.next = node
        
        self.length += 1

    def traverse(self):
        if self.head is None:
            return False
        else:
            node = self.head
            while node:
                print(node.value)
                node = node.next

    def search(self, nodeValue):
        if self.head is None:
            return False
        else:
            node = self.head
            while node:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return False

    def removeAt(self, index):
        currNode = self.head
        prevNode = None
        currIndex = 0

        if index > self.length or index < 0:
            return False

        if index == 0:
            self.head = currNode.next
        else:
            while currIndex < index:
                currIndex += 1
                prevNode = currNode
                currNode = currNode.next

            prevNode.next = currNode.next
        
        self.length -= 1
        return currNode.value



ll = SinglyLinkedList()

# ll.insert(0, 0)
# ll.insert(1, 1)
# ll.insert(2,1)
# ll.insert(3,1)
# ll.insert(4,0)
    
ll.addAt(0, 0)
ll.addAt(1, 0)
ll.addAt(2,1)
ll.addAt(3,2)
ll.addAt(4,0)
ll.addAt(6, 4)

ll.removeAt(3)

         
print([node.value for node in ll])               
# ll.traverse()
print(ll.search(3))