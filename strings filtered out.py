list=[1,2,'a','b',"5",9,"6"]
i=0
a=[]
while i<len(list):
    if type(list[i])==str:
        a.append(list[i])
    i=i+1
print(a)


# second method
list=[1,2,'a','b',16,"5",9]
i=0
a=[]
while i<len(list):
    if type(list[i])==int:
        new_list=list[i]
        a.append(new_list)
    i=i+1
print(a)
