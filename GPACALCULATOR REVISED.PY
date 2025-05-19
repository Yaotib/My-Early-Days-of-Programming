#Grade to points mapping
grades = {
    "A":4.0,
    "B+":3.5,
    "B":3.0,
    "C+":2.5,
    "C":2.0,
    "D":1.0,
    "F":0.0
}

#Asking number of courses
courses = int(input('How many courses do you offer:'))

total_points = 0.0
total_credit = 0.0

for i in range(1,courses +1):
    print(f'course{i}')
    credit = int(input('Credit:'))
    grade = input('Grade:').upper()
if grade in grades:
    total_points += grades[grade]* credit
    total_credit += credit

else:
    print('Invalid !')

#CALCULATING GPA
gpa = total_points / total_credit
print(f'GPA:{gpa}')