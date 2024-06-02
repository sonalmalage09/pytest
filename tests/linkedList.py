class Node:
    def __init__(self, data=None, pointer=None):
        self.data = data
        self.pointer = pointer

    def setData(self, data):
        self.data = data

    def setNext(self, pointer):
        self.pointer = pointer

    def getData(self):
        return self.data

    def getNext(self):
        return self.pointer

    def hasNext(self):
        return self.pointer is not None


class LinkedList(object):
    def __init__(self, node=None):
        self.length = 0
        self.head = node

    def length(self):
        current = self.head
        count = 0
        while count > 0:
            count += 1
            current = current.pointer
        return count

    def insertAtBegin(self, data):
        newNode = Node()
        newNode.data = data
        if self.length == 0:
            self.head = newNode
        else:
            newNode.pointer = self.head
            self.head = newNode
        self.length += 1

    def insertAtEnd(self, data):
        newNode = Node()
        newNode.data = data
        current = self.head
        while current.pointer is not None:
            current = current.pointer
        current.pointer = newNode
        self.length += 1

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.pointer

    def deleteAtEnd(self):
        if self.length == 0:
            print("List is empty")
        else:
            currentNode = self.head
            previousNode = self.head
            while currentNode.pointer is not None:
                previousNode = currentNode
                currentNode = currentNode.pointer
            previousNode.pointer = None
            self.length -= 1


if __name__ == "__main__":
    sonal = LinkedList()
    size = int(input("Enter number values to be added to linkedList:"))
    print("Enter {} values".format(size))
    count=0
    while count<size:
        val=input()
        sonal.insertAtEnd(int(val))
        count+=1
    print("Elements are:")
    sonal.display()

