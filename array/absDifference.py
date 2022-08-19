nums = [1,3,5,6,7,8]

oddSum = 0
evenSum = 0

for n in nums:
	if n%2==0:
		evenSum +=n
	else:
		oddSum +=n

res = oddSum - evenSum 

if res<0:
    res *=-1

print(res)
