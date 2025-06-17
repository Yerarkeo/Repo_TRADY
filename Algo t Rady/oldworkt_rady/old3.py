def countOddNumber(array):
    counter=0
    for i in array:
        if i % 2!=0:
            counter+=1
    return counter
arr1=[2,4,5,6,7,9]
arr2=[3,5,6]
arr3=[4,8,9,2,1]
print(countOddNumber(arr1))
print(countOddNumber(arr2))
print(countOddNumber(arr3))
# ex2
arr1=[5,6,56,6,7,9]
arr2=[3,5,7,9,8]
arr3=[4,8,3,2,1,7,3,9]
# ex1:
arrAll=arr1+arr2+arr3
min=arrAll[0]
for i in range(len(arrAll)):
    if arrAll[i]<min:
        min=arrAll[i]
print('minimum is:',min)
# ex2:
arrAll=arr1+arr2+arr3
sumAll=0
for i in range(len(arrAll)):
    if arrAll[i]%2==0:
        sumAll+=arrAll[i]
print('sumAllEven:',sumAll)
# ex3:
arrAll=arr1+arr2+arr3
reverse=[]
for i in range(len(arrAll)):
    reverse.insert(0,arrAll[i])
print( reverse)
# ex4:
arrAll=arr1+arr2+arr3
arrAll.append(100)
print(arrAll)
# ex5:
arrAll=arr1+arr2+arr3
for i in range(len(arrAll)):
    if arr1==7:
        arr1=10
    if arr2==7:
        arr=20
    if arr2==7:
        arr=30
print(arrAll)



