arr = [1,2,3,4,5,6]

k = 2
k = k%len(arr)

for i in range(k):
	val = arr[-1]
	for j in range(len(arr)-1, 0,-1):
		arr[j]=arr[j-1]
	
	arr[0]=val

print(arr)


nums = [1,2,3,4,5,6,7]

i, j = 0, len(nums)-1

while i<j:
    nums[i], nums[j] = nums[j], nums[i]
    i +=1


print(nums)
