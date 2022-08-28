class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Root: {self.val} Left: {self.left.val} right: {self.right.val}"

s = "ab*c/ef/g*+k+xy*-"

stack = []
array = ["*","/","+","-"]
operator = set(array)



for c in s:
    if c in operator:
        right = stack.pop()
        left = stack.pop()
        node = Node(c, left, right)
        stack.append(node)
    else:
        stack.append(c)



print(stack, len(stack))

