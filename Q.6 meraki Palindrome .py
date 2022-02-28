string=input("enter the string")
l1=list(string)
l=len(l1)
i=-1
a=[]
while i>=-l:
    a.append(l1[i])
    i-=1
if a==l1:
    print("palindrome")
else:
    print("not palindrome")
print(a)
