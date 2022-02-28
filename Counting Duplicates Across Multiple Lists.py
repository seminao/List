

name = ['Jack','Ben','Jack','Ben','Jack','Jack']
age = [25,25,34,25,25,34]
height = [180,180,200,180,180,200]
i=0
b=[]
f=[]
d=[]
c1=0
c2=0
c3=0
s=0
avg=0
while i<len(name):
    if name[i] not in b:
        c1+=1
        b.append(name[i])
    elif age[i] not in f:
        c2+=1
        f.append(age[i])
    elif height[i] not in d:
        c3+=1
        d.append(height[i])
    s=c1+c2+c3
    avg=s//3
    i=i+1
print(avg)
    

