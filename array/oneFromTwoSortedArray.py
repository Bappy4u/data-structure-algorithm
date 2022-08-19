l,r=0,0
arr1 = [1,3,5]
arr2 = [2,4,6]
res = []
while l<len(arr1) and r<len(arr2):
	if arr1[l]<arr2[r]:
		res.append(arr1[l])
		l +=1
	else:
		res.append(arr2[r])
		r +=1

if l==len(arr1):
	res +=arr2[r::]
else:
	res +=arr1[l::]

print(res)