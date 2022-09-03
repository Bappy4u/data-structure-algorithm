class Node:
    def __init__(self,id) -> None:
        self.id = id
        self.children = []
        self.parent = -1
    def addChild(self,node):
        if node not in self.children:
            self.children.append(node)
    def __repr__(self) -> str:
        return f"Node: {self.id}"

       

list = [[0,-1],[1,0],[2,1],[3,1],[4,1],[6,1],[7,1],[8,2],[9,5],[10,11]]

roots = []

hash = {}
def find_or_create(nid):
    if not hash.get(nid):
        hash[nid] = Node(nid)
    return hash[nid]


for id,parentId in list:
    child_node = find_or_create(id)
    if parentId==-1:
        roots.append(child_node)
        continue
    
    parent_node = find_or_create(parentId)

    parent_node.addChild(id)
    child_node.parent = parentId
   
    
    if parent_node not in roots and parent_node.parent ==-1:
        roots.append(parent_node)
    if child_node in roots:
        roots.remove(child_node)



print(len(roots))

for root in roots:
    print(root)
    for node in root.children:
        print("\t", hash[node])