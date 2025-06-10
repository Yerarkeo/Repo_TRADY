string='banana'
h=len(string)-1
result=""
for i in range(len(string)):
    result +=string[h-i]
print(result)