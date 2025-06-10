arr1=[2,4,5,6,7,9]
arr2=[3,5,6,]
arr3=[4,8,9,2,1]
sum=0
sum1=0
sum2=0
sum3=0
for i in range(len(arr1)):
    sum1+=arr1[i]
for u in range(len(arr2)):
    sum2+=arr2[u]
for o in range(len(arr3)):
    sum3+=arr3[o]
sum==sum1+sum2+sum3

print(sum)