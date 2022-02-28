numbers=[1,1,1,1,1,1,1,1,1]
i=0
max=0
sec=0
while i<len(numbers):
    if numbers [i] >max:
        max=numbers[i]
    if numbers[i]<max and numbers[i]>sec:
        sec=numbers[i]
    i=i+1
print(sec)
# print(max)
