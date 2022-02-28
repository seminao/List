num = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even_s=0
odd_s=0
avg=0
avg1=0
even_c=0
odd_c=0
while i<len (num):
    if num[i]%2==0:
        even_s=even_s+num[i]
        even_c=even_c+1
        avg=even_s//even_c
    else:
        odd_s=odd_s+num[i]
        odd_c=odd_c+1
        avg1=odd_s//odd_c
    i=i+1
print("avg of even",avg)
print("avg of odd",avg1)