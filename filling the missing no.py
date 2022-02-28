nums=[ 1,3,6,7,48]
i=1
while i<nums[-1]:
    if i not in nums:
        nums.append(i)
        nums.sort()
    i=i+1
print(nums)







