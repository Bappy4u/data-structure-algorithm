class Node:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right




"""class Tree:
    def __init__(self, root) -> None:
        self.__root = Node(root)

    def addNode(self,val):
        root = self.getRoot()


    def getRoot(self):
        return self.__root
    
"""
    
    
arr = [3,5,2,1,4,6,7]
root = Node(arr[0])

que = [root]
i = 0
res = []
while i<len(arr):
    qlen = len(que)

    for j in range(qlen):
        x = que.pop(0)
        res.append(x)
        
        i +=1
        if i==len(arr):
            break
        x.left = Node(arr[i])
        res.append(arr[i])
        i +=1
        if i==len(arr):
            break
        x.right = Node(arr[i])
        res.append(arr[i])

        que.append(x.left)
        que.append(x.right)




res = []   
def height(root):
    if not root:
        return 0

    left=  height(root.left)
    right=  height(root.right)
    
    return 1+ max(left,right)
        


print(f" height: {height(root)}")      






