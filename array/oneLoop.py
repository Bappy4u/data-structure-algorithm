n = int(input())


#10 9 8 7 6 5 4 3 2 1 2 3 4 5 6 7 8 9

for i in range(n, -n-1, -1):
    if i!=0 and i != -1:
        print(abs(i), end=" ")
    
