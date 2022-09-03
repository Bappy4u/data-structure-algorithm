class Node:
    def __init__(self,id) -> None:
        self.id = id
        self.children = []
        self.parent = None
    def addChild(self,node):
        if node not in self.children:
            self.children.append(node)
    def __repr__(self) -> str:
        return f"Node: {self.id}"

       

list = [[1,0],[2,1],[3,1],[4,1],[6,1],[7,1],[8,2],[9,5],[10,11]]

roots = []

hash = {}
def find_or_create(nid):
    if hash.get(nid):
        return hash[nid]
    else:
        return Node(nid)


for id,parentId in list:

    child_node = find_or_create(id)
    parent_node = find_or_create(parentId)

    parent_node.addChild(child_node)
    child_node.parent = parent_node
   
    hash[id]=child_node
    hash[parentId] = parent_node
    if parent_node not in roots:
        roots.append(parent_node)
    if child_node in roots:
        roots.remove(child_node)




    




for root in roots:
    print(root)
    for node in root.children:
        print("\t", node)