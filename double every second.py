
n=[1,23,3,42,5,64,7,18,9,10]
i=0
a=[]
while i<len(n):
    if i%2!=0:
        a.append(n[i]+2)
    else:
        a.append(n[i])
   
    i=i+1
print(a)

