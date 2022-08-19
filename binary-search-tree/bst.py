
class Node:
    def __init__(self, val,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right



root = Node(0)


arr = [1,2,3,4,5,6,7,8]

def addNode(val, r1:Node):
    if not r1.left and not r1.right:
        if val<r1.val:
            r1.left = Node(val)
        else:
            r1.right = Node(val)
        return

    if val<r1.val:
        if not r1.left:
            r1.left = Node(val)
            return 
        addNode(val, r1.left)
    else:
        if not r1.right:
            r1.right = Node(val)
            return
        addNode(val, r1.right)

def deleteNode(val,temp):
    if not temp:
        return
    if temp.left and val==temp.left.val:
        node = temp.left
        if not temp.left.left and not temp.right.right:
            temp.left = temp.left.left
            return
        elif not temp.left.left:
            temp.val = temp.left.val
            temp.left = temp.left.left
        else:
            if temp.right:
                temp.right
                while True:
                    if temp.left:
                        if not temp.left.left:
                            node.val = temp.left.val
                            temp.left = temp.right
                            
    """if temp.right and val==temp.right.val:
        temp.right = None
        return

    if val<temp.val:
        deleteNode(val, temp.left)

    else:
        deleteNode(val, temp.right)
"""
    

for i in arr:
    addNode(i, root)


temp = root

def bst(temp):
    if temp:
        bst(temp.left)
        print(temp.val, end="")
        bst(temp.right)


bst(temp)
temp = root
deleteNode(0, temp)

bst(temp)