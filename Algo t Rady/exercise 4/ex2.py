student_score = [90, 49, 68, 40, 92, 50, 45, 59]
counter=0
for i in range(len(student_score)):
    if student_score[i]>80:
        counter+=1
print(counter)