class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def insert(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next

            lastNode.next = newNode
    def print(self):
        data = self.head
        while data:
            print(data.data)
            data = data.next




linkList = LinkedList()
linkList.insert(Node("Najmul"))
linkList.insert(Node("Hossain"))
linkList.insert(Node("Bappy"))
linkList.print()
