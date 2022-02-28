# *****string Method**********
a=234567
string=str(a)
b=([string])
print(b)

digit=12345
string=str(digit)
i=0
a=[ ]
while i<len(string):
    a.append(string[i])
    i=i+1
print(a)

digit=12345
a=str(digit)
print("'"+a+"'")

# *****join Method**********
name=["seminao"]
string="".join(name)
i=0
c=0
a=[]
while i<len(string):
    a.append(string[i])
    i=i+1
print (a)

name=["seminao"]
string="".join(name)
i=0
while i<len(string):
    i=i+1
print(string)

# o/p="this is awesome"
a=["this","is","great"]
b=" ".join(a)
i=0
while i<len(b):
    i=i+1
print("'",b,"'")

# *****split Method**********
list=("seminao onring vilychon")
list1=list.split()
i=0
while i<len(list1):
    i+=1
print(list1)

a=("seminao onring")
list1=a.split()
i=0
while i<len(list1):
    i=i+1
print(list1)

n=[1,2,3,4,5,6]
b=str(n).split(",")
print(b)

# *****Append Method**********
n=[1,2,3,4,5,6]
i=0
a=[]
while i<len(n):
    if type (n[i])==int:
        a.append(str(n[i]))
        b=" ".join(a)
    i=i+1
print([b])

a=["abcd","are","anyone","always"]
i=0
c=[]
while i<len(a):
    b=0
    while b<len(a[i]):
        if a[i][b]==a[i][0]:
            d=a[i][0]
            c.append(d)
        b+=1
    i=i+1
print(c)
# *****replace Method**********
n=[1,2,3,4,5,6]
i=0
while i<len(n):
    b=str(n).replace(",","")
    i+=1
print(b)
             
# *****strip Method**********
txt = " Hello World "
x = txt.strip()
print(x)

n=["shangkham","seminao","shangyaiphy"]
i=0
a=1
while i<len(n):
    print(a,":",n[i])
    a+=1
    i+=1

# *****strip Method**********
a=[1,1,1,1,1,1,1,1]
i=0
while i<len(a):
    a.sort()
    i+=1
print(a[-2])