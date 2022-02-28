nums=[ 1,3,5,6,7,8]
i=0
while i<len(nums):
    if nums[i]==1:
        nums.insert(1,2)
        nums.insert(3,4)
    i=i+1
print(nums)
