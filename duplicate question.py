a=[12,18,16,14,12]
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i+=1
print(b)
# second method
n = [19, 17, 12, 17, 17, 18, 10, 17, 14, 12, 19, 17, 12, 13, 11]
i=0
a=[]
while i<len(n):
    if n[i]not in a:
        a.append(n[i])
    i=i+1
print(a)