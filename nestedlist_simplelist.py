# simple
list1=[["g","f","g",],["i","s"],["b","e","s","t"]]
i=0
str=""
while i<len(list1):
  j=0
  while j<len(list1[i]): 
    str=str+list1[i][j]
    j=j+1
  i=i+1
print(str)  

# second method
list1=[["g","f","g",],["i","s"],["b","e","s","t"]]
i=0
a=[]
b=0
while i<len(list1):
  if type(list1[i])==type([]):
    j=0
    while j<len(list1[i]):
      a.append(list1[i][j])
      j=j+1
  else:
    a.append(list1[i])
  i=i+1
  b="".join(a)
print(b)