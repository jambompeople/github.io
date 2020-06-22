nums = [2,7,11,15]
target = 9
for x in range(0,len(nums)):
    for y in range(0,len(nums)):
        if(nums[x]+nums[y]==target):
            print([x,y])
            break