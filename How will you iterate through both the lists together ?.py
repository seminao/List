students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
marks = [10, 20, 56, 45, 36, 20]
length = len(students) 
c = 0
s=0
d=0
while c < length:
    d=students[c]+str(marks[c])
    print(d)
    c+=1