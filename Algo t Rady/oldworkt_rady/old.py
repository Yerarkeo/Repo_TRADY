students=[
    {'id':1, 'name':'Alice','age':18,'class':'A', 'score':85},
    {'id':2, 'name':'Bob','age':17,'class':'B','score':90},
    {'id':3,'name':'Charlie','age':18,'class':'C','score':49},
    {'id':4,'name':'Dara','age':19,'class':"A",'score':92},
    {'id':5,'name':'Eve','age':17,'class':'C','score':88}
]
# # q1
for student in students:
    print(student['name'])
# # q2
sum=0
for i in range(len(students)):
    sum+=students[i]['age']
print(sum/len(students[i]))
# # q3
counter=0
for i in range(len(students)):
    if students[i]['class']=='C':
        counter+=1
print(counter)
# # q4
count=0
for i in range(len(students)):
    if students[i]['class']=='A'or students[i]['class']=='B':
        count+=1
print(count)
# q5
max=students[0]['score']
for i in range(len(students)):
    if students[i]['score'] > max:
        max=students[i]['score']
print(students[i]['name'],max)
# q6:
for i in range(len(students)):
    if students[i]['score'] < 50:
        print(students[i]['name'],students[i]['score'])
# q7:
sum=0
for i in range(len(students)):
    sum+=students[i]['score']
print(sum/len(students[i]))
# q0
students[i].pop('score')
print(students[i])
