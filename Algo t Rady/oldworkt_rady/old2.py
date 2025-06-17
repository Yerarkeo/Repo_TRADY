arr1=[2,4,5,6,7,9]
arr2=[3,5,6,]
arr3=[4,8,9,2,1]
# ex1:
sumAll=0
sum1=0
sum2=0
sum3=0
for i in range(len(arr1)):
    sum1+=arr1[i]
print(sum1)
for u in range(len(arr2)):
    sum2+=arr2[u]
print(sum2)

for o in range(len(arr3)):
    sum3+=arr3[o]
print(sum3)
sumAll=sum(arr1)+sum(arr2)+sum(arr3)
print('sumAll:',sumAll)
# ex2:
allArrays=arr1+arr2+ arr3
allArr=[]
for i in range(len(allArrays)):
    if allArrays[i]%2==1:
        allArr.append(allArrays[i])
print(allArr)
# ex3:
arrAll=arr1+arr2+arr3
sumAll=sum(arr1)+sum(arr2)+sum(arr3)
counter=0
for i in range(len(arrAll)):
    counter+=1
print(sumAll/counter)
# ex4:
arrAll=arr1+arr2+arr3
max=arrAll[0]
for i in range(len(arrAll)):
    if arrAll[i]>max:
        max=arrAll[i]
print('maximum is :', max)
# ex5:
arrAll=arr1+arr2+arr3
for i in range(len(arrAll)):
    if arrAll[i]%2==0:
        arrAll[i]=100
print(arrAll)



