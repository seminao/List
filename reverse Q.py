# *******reverse**********
animal=["tail", "body", "head"]
l=len(animal)-1
i=l
while i>=0:
    print(animal[i])
    i=i-1
# *******reverse**********
l=[1,2,3,4,5]
i=1
a=[]
while i<=len(l):
    a.append(l[-i])
    i=i+1
print(a) 
# *******reverse**********
places=["delhi","gujrat","rajesthan","punjab","kerala"]
l=len(places)-1
i=l
while i>=0:
    print(places[i])
    i=i-1
# *******reverse**********
n=int(input("enter the number"))
rev=str(n)
b=" "
i=-1
while i>=-len(rev):
    b=b+rev[i]
    i=i-1
print(b)

