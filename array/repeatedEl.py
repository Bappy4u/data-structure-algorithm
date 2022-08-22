arr = [1,1,2,3,4,5,5,5,6,6,6,6,6,6,]

arr.sort()

i = 0

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


dic = {key:0 for key in arr}

for n in arr:
    dic[n] +=1

for d in dic:
    if dic[d]>1:
        print(d)