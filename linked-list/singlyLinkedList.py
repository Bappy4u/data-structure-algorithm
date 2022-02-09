class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insertEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next

            lastNode.next = newNode  


    def insertAt(self, pos, node):
        if self.head is None:
            return
        else:
            currPosition = 0
            currNode = self.head
            prevNode = currNode
            while True:
                if currPosition == pos:
                    node.next = currNode
                    prevNode.next = node
                prevNode = currNode
                currNode = currNode.next
                currPosition +=1
            


    def insertHead(self, newNode):
        tempNode = self.head
        self.head = newNode
        self.head.next = tempNode
        del tempNode

    def print(self):
        data = self.head
        while data:
            print(data.data)
            data = data.next
    




linkList = LinkedList()
linkList.insertEnd(Node(20))
linkList.insertEnd(Node(40))
linkList.insertEnd(Node(60))
linkList.insertHead(Node(10))
linkList.insertAt(1, Node(30))
linkList.print()