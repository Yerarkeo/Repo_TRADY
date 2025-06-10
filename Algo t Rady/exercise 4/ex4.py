student_score = [90, 49, 68, 40, 92, 50, 45, 59]
for i in range(len(student_score)):
    if student_score[i]<=45 and student_score[i]<50:
        student_score[i]=50
print(student_score)