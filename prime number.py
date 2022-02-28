list=[1,4,67,89,34,56,6,2,6,7]
a=[]
i=1
while i<len(list):
    count=0
    j=2
    while j<=list[i]//2:
        if list[i]%j==0:
            count+1
            break
        j=j+1
    if count==0 and list[i]!=1:
        a.append(list[i])
    i+=1
print(a)