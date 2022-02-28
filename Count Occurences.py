
alp= ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
a=[]
while i<len(alp):
    c=0
    j=0
    b=[]
    while j<len(alp):
        if alp[i]==alp[j]:
            c=c+1
        j=j+1
    b.append(alp[i])
    b.append(c)
    if b not in a:
        a.append(b)
    i=i+1
print(a)