list=[1,7,[6,[0,9,5,[3,2,9,[0]]]]]
a=list[0]
b=list[2][1][0]
c=list[2][1][3][1]
d=list[2][1][0]
e=list[2][1][2]
print(a,",",b,",",c,",",d,",",e)

# o/p=6,9,14,1,3
list=[[5,6,7,8,[9,10,11,12,14],1,2],3,4]
a=list[0][1]
b=list[0][4][0]
c=list[0][4][4]
d=list[0][5]
e=list[1]
print(a,",",b,",",c,",",d,",",e)

# o/p=11,13,16,[17]
list=[[10,11,12,[13,14,15],16,[17],18,19]]
a=list[0][1]
b=list[0][3][0]
c=list[0][4]
d=list[0][5]
print(a,",",b,",",c,",",d)

list=[[[10,20],[40],[30,50,60,[10,14,15,[9],25]]]]
a=list[0][0]
# b=list[1]
print(a)

# o/p=3,13,[10],12
list=[1,[1,2,3],[4,5,6,[7,8,9,[10],11],12,13]]
a=list[1][2]
b=list[2][5]
c=list[2][3][3]
d=list[2][4]
print(a,",",b,",",c,",",d)

