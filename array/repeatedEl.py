arr = [1,2,3,4,5,6]

arr.sort()


res = []
while i<len(arr):
    temp = arr[i]
    j = i+1
    while j<len(arr):
        if arr[i]==arr[j]:
            j +=1
        else:
            break
    
    if i+1 !=j:
        res.append(arr[i])

    i = j

print(res)

        
