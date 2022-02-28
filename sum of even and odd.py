n = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
s=0
m=0
while i<len(n):
    if n[i]%2==0:
        s=s+n[i]
    else:
        m=m+n[i]
    i=i+1
print("sum of even",s)
print("sum of odd ",m)