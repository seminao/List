list=[
     [8,3,4],
     [1,5,9],
     [6,7,2]
     ]
i=0 
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
while i<len(list):
     a=a+list[0][i]
     b=b+list[1][i]
     c=c+list[2][i]
     d=d+list[i][0]
     e=e+list[i][1]111
     f=f+list[i][2]
     g=g+list[i][i]
     h=h+list[i][2-i]
     i=i+1
if a==b==c==d==e==f==g==h:
     print("Magic Square")
else:
     print("Not Magic Squa")