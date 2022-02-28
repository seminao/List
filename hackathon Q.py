###Q4.reverse
digit=7576
a=str(digit)
b=list(a)
c=[]
i=-1
while i>=-len(b):
    c.append(int(a[i]))
    i-=1
print(c)


# Q10.
from re import L
list1=["tail","body","top"]
l=len(list1)-1
i=l
while i>=0:
    print(list1[i])
    i=i-1

# Q13.duck duck goose.
duck=["a","b","c","d","e","f"]
i=0
a=[]
while i<len(duck):
    if duck[i]==duck[5]:
        a.append(duck[i])
    i=i+1
print(a)








