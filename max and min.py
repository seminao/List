n=[345,5,644,35,653,3]
i=0
min=n[0]
while i<len(n):
    if n[i]<min:
        min=n[i]
    i=i+1
print(min)

# max list
n=[345,5,644,35,653,3]
i=0
max=0
while i<len(n):
    if n[i]>max:
        max=n[i]
    i=i+1
print(max)