n=[[0],[1,2,3],[6,7,8,10,11],[23,24]]
i=0
max=0
while i<len(n):
    j=0
    c=0
    while j<len(n[i]):
        c=c+1
        if c>max:
            max=c
            s=n[i]
        j=j+1
    i=i+1
print(max,s)

# second method
n=[[0],[1,2,3],[6,7,8,10,11],[23,24]]
i=0
a=[]
while i<len(n):
    c=0
    j=0
    while j<len(n[i]):
        c=c+1
        j=j+1
    i=i+1
    a.append(c)
print(a)
# third method
n=[[0],[1,2,3],[6,7,8,10,11],[23,24]]
i=0
ad=[]
while i<len(n):
    ad.append(len(n[i]))
    i=i+1
print(ad)