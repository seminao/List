

# using append and sum
n=[10,10,20,10]
n=int(input("enter the number"))
a=[]
i=0
sum=0
while i<n:
    n1=int(input("enter the number"))
    a.append(n1)
    sum=sum+a[i]
    i=i+1
print(a)
print(sum)

# o/p=3
# counting first value same more than 2 element
a=["axa","a","ab","aba","xyzx","aba"]
i=0
while i<len(a):
    j=0
    c=0
    while j<len(a[i]):
        if a[i][j]==a[i][j]:
            c=c+1
        j=j+1
    i=i+1
print(c)

# o/p:room 1:1.marmaid
            # 2.dora
    # room  2:1.chindrella
    #          2.tinkerbell
    #  room 3:1.snowwhite
            # 2.unicorn
name=["marmaid","dora","chindrella","tinkerbell","snowhite","unicorn"]
room=[1,2,3]
i=0
s=0
x=2
while i<len(room):
    print("room:",room[i])
    j=s
    a=1
    while j<x:
        print(a,".",name[j])
        j+=1
        a+=1
    x+=2
    i+=1
    s+=2

# o/p:[1,1,1,1,1,1,1,1,1]
n=[1,2,3,4,5,6,7,8,9,10]
i=0
c=1
d=[]
while i<=len(n):
    b=n[i-c+1]
    d.append(b)
    c+=1
    i=i+1
print(d)

# entering no.output string
a=["a","b","c","d","e","f","g","h","i","j","k"]
user=int(input("enter the number"))
i=1
while i<len(a):
    j=i
    while j<=user:
        if i==user:
            print(a[i-1])
        j=j+1
    i=i+1

name1=(input("enter the name1"))

# using many method
list=["apple ","it", "so", "sweet"]
n=" ".join(list)
str="it"
replace="is"
string=str.split()
i=0
a=[]
while i<len(n):
    if str in string:
        string.remove(str)
    i=i+1
    b=n.replace(str,replace)
print(b)





