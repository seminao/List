a=[1,4,23,"3","76",7,10]
i=0
b=[]
c=[]
d=0
while i<len(a):
    if type(a[i])==int:
        b.append(a[i])
    if type (a[i])==str:
        c.append(int(a[i]))
    d=b+c
    j=0
    s=0
    while j<len(d):
        s=s+d[j]
        j=j+1
    i=i+1
print(s)




