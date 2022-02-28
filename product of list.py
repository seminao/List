n=int(input("enter the number"))
a=[]
i=0
product=1
while i<n:
    n1=int(input("enter the number"))
    a.append(n1)
    product=product*a[i]
    i=i+1
print(a)
print(product)
