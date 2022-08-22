class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


arr = [1,2,3,4,5,6,7]
root = TreeNode(arr[0])

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
        x.left = TreeNode(arr[i])
        res.append(arr[i])
        i +=1
        if i==len(arr):
            break
        x.right = TreeNode(arr[i])
        res.append(arr[i])

        que.append(x.left)
        que.append(x.right)

print(len(res))


res = []   
def bst(val):
    if val:
        bst(val.left)
        res.append(val.val)
        bst(val.right)
        

bst(root)


print(res)      






