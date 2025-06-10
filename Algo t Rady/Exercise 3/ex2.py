student_ages = [15, 18, 20, 17, 16, 25]
max=student_ages[0]
for i in range(len(student_ages)):
    if student_ages[i]>max:
        max=student_ages[i]
print(max)