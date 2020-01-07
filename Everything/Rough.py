def twoSum(nums,target):
    a=len(nums)
    for y in range(a-1):
        for x in range(a-1):
        	#print(y,x+1)
        	if (x+1)<=y:
        		continue
        	elif (nums[y]+nums[x+1]) == target:
        		print([y,x+1])

nums=[2,7,1,15]
target=16

twoSum(nums,target)