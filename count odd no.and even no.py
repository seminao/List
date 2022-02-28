n = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
a=[]
b=[]
c=0
m=0
while i<len(n):
    if n[i]%2==0:
        c=c+1
        b.append(c)
    else:
        m+=1
        a.append(m)
    i=i+1
print("even no.",c)
print("odd n.",m)
