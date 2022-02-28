n=[2,3,4,[4,2,4],[6,["a","b"],3],[7,4]]
i=0
a=[]
while i<len(n):
    if type(n[i])== type([]):
        j=0
        while j<len(n[i]):
            if type(n[i][j])==type([]):
                k=0
                while k<len(n[i][j]):
                    a.append(n[i][j][k])
                    k=k+1
            else:
                a.append(n[i][j])
            j=j+1
    else:
        a.append(n[i])
    i=i+1
print(a)
# third 
a=[1,4,9,[2,[5,7,6],6],3]
i=0
b=[]
while i<len(a):
    if type(a[i])==type([]):
        j=0
        while j<len(a[i]):
            if type(a[i][j])==type([]):
                k=0
                while k<len(a[i][j]):
                    b.append(a[i][j][k])
                    k+=1
            else:
                b.append(a[i][j])
            j+=1
    else:
        b.append(a[i])
    i=i+1
print(b)   


# second question
a=[1,[1,2,3],[4,5,6,[7,8,9,[10],11],12,13]]
i=0
b=[]
while i<len(a):
    if type(a[i])==type([]):
        j=0
        while j<len(a[i]):
            if type (a[i][j])==type([]):
                k=0
                while k<len(a[i][j]):
                    if type (a[i][j][k])==type([]):
                        l=0
                        while l<len(a[i][j][k]):
                            b.append(a[i][j][k][l])
                            l=l+1
                    else:
                        b.append(a[i][j][k]) 
                    k+=1
            else:
                b.append(a[i][j]) 
            j+=1
    else:
        b.append(a[i]) 
    i+=1
print(b)     
