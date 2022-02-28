num = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even_c=0
odd_c=0
total_c=0
odd_s=0
even_s=0
total_s=0
avg_odd=0
avg_even=0
total_avg=0
a=[]
while i<len(num):
    if num[i]%2==0:
        even_c+=1
        even_s=even_s+num[i]
        avg_even=even_s//even_c
    elif num[i]%2!=0:
        odd_c+=1
        odd_s=odd_s+num[i]
        avg_odd=odd_s//odd_c
    total_c=even_c+odd_c
    total_s=even_s+odd_s
    total_avg=total_s//total_c
    i=i+1
print("even_c=",even_c)
print("odd_c=",odd_c)
print("total_c=",total_c)
print("even_s=",even_s)
print("odd_s=",odd_s)
print("total_s=",total_s)
print("avg_even=",avg_even)
print("avg_odd=",avg_odd)
print("total_avg=",total_avg)
        