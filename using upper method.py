name1=(input("enter the number 1"))
name2=(input("enter the number2"))
name3=(input("enter the number3"))
i=0
a=[]
while i<len(name1) and i<len(name2):
    if name1[i]==name1[0] and name2[i]==name2[0]:
        b=name1[i].upper()
        c=name2[i].upper()
        d=b+c
        a.append(d)
        f=".".join(a)
    i=i+1
print(f+name3)

# second method
name1=(input("enter the name1"))
name2=(input("enter the number2"))
name3=(input("enter the number3"))
b=""
i=0
while i<len(name1) and i<len(name2):
    if name1[i]==name1[0] and name2[i]==name2[0]:
        cap=name1[i].upper()
        cap1=name2[i].upper()
        b+=cap+"."+cap1
    i=i+1
print(b+"."+name3)
# third method
list=["ramchanphy","pooja"]
str=""
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        if list[i][j]==list[i][0]:
            x=list[i][0].upper()
            str+=x+"."
        j+=1
    i+=1
print(str[0:3])
