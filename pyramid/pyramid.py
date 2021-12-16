"""
*..
**.
***
"""
for i in range(3):
    for j in range(3):
        if j <= i:
            print("*", end="")
        else:
            print(".", end="")

    print("")


print("-----------------")
n = 3
for i in range(n):
    for j in range(n):
        if i+j < n:
            print("*", end="")
        else:
            print(".", end="")

    print("")


print("-----------------")

# row should be a even number
row = n*2
col = row - 1
for i in range(0, row, 2):
    st, end = col//2 - i//2, col//2 + i//2
    for j in range(col):

        if j>=st and j<=end:
            print("*", end="")
        else:
            print(".", end="")

    print("")