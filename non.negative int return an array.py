n=86043
i=0
digit=[]
while n>0:
    digit.append(n%10)
    n//=10
    i+=1
print(digit[::-1])