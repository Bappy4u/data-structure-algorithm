class Node:
    def _init__(self,id,name,parentId, left=None, right =None):
        self.id = id
        self.val = name
        self.parentId = parentId
        self.left = left
        self.right = right




list = [[1,"root", -1],[2,"node", 1],[3,"node", 2],[4,"node",3 ],[5,"node", 4],[6,"node", 3]]

for l in list:
    if l[2]==-1:
        rootList = l

root = Node(l[0], l[1], l[2])



def insertNode(root, item):
    if root:
        if root.id == item[2]:
            if root.left:
                root.right
            else:
                root.left = Node(item[0],item[1],)


for item in list:
    if item[2]!=-1:
        


