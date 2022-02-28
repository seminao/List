#using while loops
numbers=[50,40,23,70,56,12,5,10,7]
i=0
count=0
while i<len(numbers):
    count=count+1
    i=i+1
print(count)

# by using slicing
numbers=[50,40,23,70,56,12,5,10,7]
i=0
count=0
while numbers[count:]:
    count+=1
print(count)




    
