str= "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
str1="over"
s="on"
i=0
while i<len(str):
    str=str.replace(str1,s)
    i=i+1
print(str)

# second method
str= "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
a=str.split(" ")
str1="over"
new_str=""
i=0
while i<len(a):
    if a[i]==str1:
        a.remove(str1)
    i=i+1
j=0
while j<len(a):
    print(a[j],end=" ")
    j=j+1
